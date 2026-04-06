from fastapi import APIRouter, HTTPException, Form, UploadFile, File, Depends
from api.schema.request import TextInput, validate_upload
from api.schema.graph import KnowledgeGraph
from api.services.extractor import TripleExtractionService
from api.services.deduplicator import DeduplicationService
from api.services.graph_builder import generate_graph
from typing import Optional

router = APIRouter(tags=["Graph Building"])

def get_extraction_service():
    service = TripleExtractionService()
    return service

_dedup_service = DeduplicationService()
def get_deduplication_service() -> DeduplicationService:
    return _dedup_service

@router.post("/build-graph", )#response_model=KnowledgeGraph)
async def build_graph(
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    service: TripleExtractionService = Depends(get_extraction_service),
    dedup_service: DeduplicationService = Depends(get_deduplication_service)
):
    if not text and not file:
        raise HTTPException(status_code=422, detail="Provide either text or a .txt file.")
    if text and file:
        raise HTTPException(status_code=422, detail="Provide only one input: either text or a .txt file.")
    
    if text:
        try:
            validated_text = TextInput(text=text)
            raw_text = validated_text.text
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raw_text = await validate_upload(file)

    try:
        raw_triples_list = await service.build_kg(raw_text)
        unique_triples_list = dedup_service.deduplicate_triples(raw_triples_list)
        # print(unique_triples_list)
        graph = generate_graph(unique_triples_list)
        # print(graph)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {
        "status": "Success", 
        "received_chars": len(raw_text), 
        "triples": [t.model_dump(by_alias=True) for t in unique_triples_list],
        "graph": graph
        }
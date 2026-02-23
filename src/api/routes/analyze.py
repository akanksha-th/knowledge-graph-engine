from fastapi import APIRouter, HTTPException, UploadFile, File, Form, logger
import json
from typing import List

from src.schemas.requests import AnalyzeRequest
# from src.services.parser_service import ParserService
from src.core.logger import get_logger
# from src.schemas.responses import AnalyzeResponse

logger = get_logger(__name__)
router = APIRouter()
# parser_service = ParserService()

@router.post("/analyze", response_model=None)
async def analyze(
    resume_file: UploadFile = File(...),
    jd_text: str = Form(...),
    github_urls: str = Form(default="[]"),
    rejection_mails: str = Form(default="[]"),
):
    try:
        pdf_content = await resume_file.read()

        github_urls_list: List[str] = json.loads(github_urls)
        rejection_mails_list: List[str] = json.loads(rejection_mails)

        request_data = AnalyzeRequest(
            jd_text=jd_text,
            github_urls=github_urls_list,
            rejection_mails=rejection_mails_list,
        )

        logger.info("Analyze request received")
        return {"message": "pipeline not wired yet"}

        
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="github_urls or rejection_mails is not valid JSON")
    except Exception as e:
        logger.error(f"Error processing analyze request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
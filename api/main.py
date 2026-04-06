from fastapi import FastAPI
from api.routes.build_graph import router as build_graph_router

app = FastAPI(
    title="Knowledge Graph Engine API",
    description="Convert your text into a knowledge graph with ease.",
    version="1.0.0",
)

@app.get("/health", tags=["Health Check"])
async def root():
    return {"status": "Success", "message": "Knowledge Graph Engine API is running."}

app.include_router(build_graph_router)

if __name__ == "__main__":
    ...
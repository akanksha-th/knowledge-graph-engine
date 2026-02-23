from fastapi import FastAPI
from src.api.routes.analyze import router
# from src.schemas.requests import 
# from src.schemas.responses import 

app = FastAPI(
    title="Shadow Resume Engine API",
    description="An API to generate shadow resumes based on user input.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Shadow Resume Engine API!"}

@app.get("/health", summary="Quick Health Check")
def health_check():
    return {"status": "healthy"}

app.include_router(
    router=router,
    prefix="/api/v1",
    tags=["analyze"],
)
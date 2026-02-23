from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Config(BaseSettings):
    # App
    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # LLM
    GROQ_API_KEY: str

    # Neo4j
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    # LangSmith
    LANGSMITH_API_KEY: str
    LANGSMITH_TRACING: bool = True
    LANGSMITH_PROJECT: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=False)
    

@lru_cache
def get_Settings() -> Config:
    return Config()
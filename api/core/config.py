from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_ignore_empty=True,
        
    )

    groq_api_key: str
    model_name: str = "llama-3.3-70b-versatile"

    # neo4j_uri: str = "bolt://localhost:7687"
    # neo4j_username: str
    # neo4j_password: str

    # langsmith_api_key: str
    # langsmith_tracing: bool = True
    # langsmith_project: str = "knowledge-graph-builder"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
from pydantic import BaseModel, field_validator, Field


class Triple(BaseModel):
    model_config = {"populate_by_name": True}
    subject: str
    predicate: str
    obj: str = Field(..., alias="object")

    @field_validator("subject", "predicate", "obj")
    @classmethod
    def validate_entries(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Subject, predicate, and object cannot be empty or whitespace")
        return v.strip()


class KnowledgeGraph(BaseModel):
    triples: list[Triple] = Field(..., min_length=1)
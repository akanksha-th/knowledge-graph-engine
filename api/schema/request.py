from pydantic import BaseModel, field_validator
from fastapi import UploadFile

MAX_TEXT_LENGTH = 8000
MAX_FILE_SIZE = 1024*1024*1     # 1MB in bytes
ALLOWED_MIME = "text/plain"


class TextInput(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Text cannot be empty.")
        if len(v) > MAX_TEXT_LENGTH:
            raise ValueError(
                f"Text exceeds {MAX_TEXT_LENGTH} characters "
                f"(got {len(v)})."
            )
        return v
    

async def validate_upload(file: UploadFile) -> str:
    if file.content_type != ALLOWED_MIME:
        raise ValueError(f"Only .txt files are allowed (got {file.content_type}).")
    
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise ValueError(f"File size exceeds 1MB (got {len(contents)} bytes).")
    
    text = contents.decode("utf-8").strip()
    if not text:
        raise ValueError("File cannot be empty."
        )
    if len(text) > MAX_TEXT_LENGTH:
        raise ValueError(
            f"Text in file exceeds {MAX_TEXT_LENGTH} characters "
            f"(got {len(text)})."
        )
    return text
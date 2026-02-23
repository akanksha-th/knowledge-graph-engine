from typing import List
from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    jd_text: str
    github_urls: List[str] = []
    rejection_mails: List[str] = []
    resume_content: str = ""

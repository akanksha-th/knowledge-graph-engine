from pydantic import BaseModel
from typing import List

class ProjectIdea(BaseModel):
    title: str
    tech_stack: List[str]
    description: str
    why_it_closes_gap: str


class RecruiterOutput(BaseModel):
    perception_risks: List[str]
    missing_competencies: List[str]
    ranked_concerns: List[str]


class StrategistOutput(BaseModel):
    reframed_bullets: List[str]
    positioning_pivots: List[str]
    project_ideas: List[ProjectIdea]


class AnalyzeResponse(BaseModel):
    shadow_skills: List[str]
    perceived_gaps: List[str]
    recruiter_view: RecruiterOutput
    strategist_output: StrategistOutput
    final_shadow_resume: str
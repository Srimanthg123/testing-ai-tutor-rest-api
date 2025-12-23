from pydantic import BaseModel

class TutorRequest(BaseModel):
    question: str
    model_type: str = "cloud"  # cloud | local

class TutorResponse(BaseModel):
    answer: str
    model_used: str
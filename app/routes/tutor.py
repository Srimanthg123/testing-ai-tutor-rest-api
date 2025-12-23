from fastapi import APIRouter

router = APIRouter()

@router.post("/explain")
def explain(payload: dict):
    prompt = payload.get("prompt", "")
    return {"response": f"Explanation for {prompt}"}


@router.post("/stream")
def stream(payload: dict):
    prompt = payload.get("prompt", "")
    return {"response": f"Streaming response for {prompt}"}


@router.post("/personalize")
def personalize(payload: dict):
    prompt = payload.get("prompt", "")
    level = payload.get("level", "beginner")
    return {"response": f"Personalized {level} explanation for {prompt}"}
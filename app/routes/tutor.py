from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.schemas import TutorRequest, TutorResponse
from app.services.cloud_llm import gemini_generate
from app.services.local_llm import local_generate
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix="/tutor", tags=["AI Tutor"])


@router.post(
    "/explain",
    response_model=TutorResponse,
    summary="Explain a concept using AI",
    description="Returns a full explanation from either a cloud or local LLM."
)
async def explain(request: TutorRequest):
    """
    Explain a given concept using an AI model.

    - **model_type**: cloud | local
    - **question**: topic to explain
    """
    try:
        if request.model_type == "cloud":
            text = ""
            async for chunk in gemini_generate(request.question):
                text += chunk
        else:
            text = local_generate(request.question)

        return TutorResponse(
            answer=text,
            model_used=request.model_type
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/explain/stream",
    summary="Stream explanation token-by-token",
    description="Streams AI-generated explanation chunk by chunk."
)
async def explain_stream(request: TutorRequest):
    """
    Streams explanation output in real time using StreamingResponse.
    """
    try:
        generator = (
            gemini_generate(request.question)
            if request.model_type == "cloud"
            else local_generate(request.question, stream=True)
        )

        return StreamingResponse(
            generator,
            media_type="text/plain"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/personalize",
    response_model=TutorResponse,
    summary="Personalized AI response",
    description="Returns a creative or personalized response using a local model."
)
async def personalize(request: TutorRequest):
    """
    Generates a personalized AI response using a local model.
    """
    try:
        response = local_generate(
            f"Personalize this explanation: {request.question}"
        )

        return TutorResponse(
            answer=response,
            model_used="local"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
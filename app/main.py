from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.routes.tutor import router, limiter

app = FastAPI(
    title="AI Tutor REST API",
    description="Streaming AI Tutor with Cloud & Local LLMs",
    version="1.0.0"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Tutor REST API running"}
from fastapi import FastAPI
from app.routes.tutor import router as tutor_router

app = FastAPI()

app.include_router(tutor_router)
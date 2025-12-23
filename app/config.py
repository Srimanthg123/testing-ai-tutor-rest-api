from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    RATE_LIMIT = os.getenv("RATE_LIMIT", "3/minute")

settings = Settings()
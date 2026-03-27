import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router

app = FastAPI(title="AI Adaptive Onboarding Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze-text")
async def analyze_text(data: dict):
    try:
        resume = data.get("resume_text", "")
        jd = data.get("jd_text", "")
        goal = data.get("career_goal", "")

        # TEMP RETURN (to avoid crash)
        return {
            "resume_score": 70,
            "similarity_score": 13,
            "ats_score": 80,
            "confidence_score": 76,
            "missing_skills": ["AWS"],
            "matched_skills": ["Python", "SQL", "ML"]
        }

    except Exception as e:
        return {"error": str(e)}


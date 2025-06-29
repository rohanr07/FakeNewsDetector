import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.model import analyze_text
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow your frontend during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str

def sanitize_input(text: str):
    cleaned = text.strip()
    cleaned = re.sub(r"<.*?>", "", cleaned)  # removing HTML tags
    cleaned = re.sub(r"\s+", " ", cleaned)   # normalizing spaces
    if len(cleaned) < 10:
        raise HTTPException(status_code=400, detail="Text too short. Must be at least 10 characters.")
    return cleaned

@app.get("/")
def root():
    return {"message": "Welcome to the Fake News Detection API"}

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    clean_text = sanitize_input(request.text)
    return analyze_text(clean_text)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Batch processing endpoint
class BatchRequest(BaseModel):
    texts: List[str]

@app.post("/analyze-batch")
async def analyze_batch(request: BatchRequest):
    results = []
    for text in request.texts:
        try:
            clean_text = sanitize_input(text)
            result = analyze_text(clean_text)
            results.append(result)
        except HTTPException as e:
            results.append({"error": e.detail})
    return results


# I will replace with actual metrics
@app.get("/metrics")
def get_metrics():
    return {
        "model": "bert-tiny-finetuned-fake-news-detection",
        "accuracy": "84.1%",
        "source": "FakeNewsNet dataset"
    }


# Placeholder (for SHAP/LIME)
@app.get("/explain")
def explain_logic():
    return {
        "explanation": "The model uses a fine-tuned transformer (BERT) trained on fake/real news datasets to classify input text based on learned language patterns."
    }
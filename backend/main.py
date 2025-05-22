from fastapi import FastAPI, Request
from model import analyze_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Fake News Detector Backend is running"}

@app.post("/analyze")
def analyze(request: Request):
    # For now, dummy output
    return {"score": 0.83, "label": "Likely Fake", "explanation": "Dummy logic"}





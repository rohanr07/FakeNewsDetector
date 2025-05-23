from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import analyze_text

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    if not request.text or len(request.text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Text is too short. Must be at least 10 characters.")
    return analyze_text(request.text)


@app.get("/health")
def health_check():
    return {"status": "ok"}
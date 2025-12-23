from fastapi import FastAPI
from ai_engine import analyze_sector

app = FastAPI()

@app.get("/analyze/{sector}")
def analyze(sector: str):
    news = "Recent market news here"
    return analyze_sector(sector, news)

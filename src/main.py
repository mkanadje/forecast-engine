from fastapi import FastAPI
from src.api.endpoints import router as api_router

app = FastAPI(title="Forecast Engine", version="0.0.1")
app.include_router(api_router)

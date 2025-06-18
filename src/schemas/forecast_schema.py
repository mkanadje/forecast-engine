from pydantic import BaseModel
from typing import List, Any


class ForecastRequest(BaseModel):
    data: List[float]
    steps: int
    model: str = "arima"


class ForecastResponse(BaseModel):
    forecast: List[float]
    model_used: str

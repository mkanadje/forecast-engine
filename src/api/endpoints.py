from fastapi import APIRouter, HTTPException
from src.schemas.forecast_schema import ForecastRequest, ForecastResponse
from src.forecasting.arima_forecast import ARIMAForecast

router = APIRouter()


@router.post("/forecast", response_model=ForecastResponse)
async def create_forecast(request: ForecastRequest):
    if request.model == "arima":
        forecast_model = ARIMAForecast()
    else:
        raise HTTPException(status_code=400, detail="Unsupported model type")
    forecast_model.fit(request.data)
    result = forecast_model.predict(steps=request.steps)
    return ForecastResponse(forecast=result, model_used=request.model)

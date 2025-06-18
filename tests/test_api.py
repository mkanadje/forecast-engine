from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_arima_forecast():
    payload = {"data": [1.0, 2.0, 3.0, 4.0, 5.0], "steps": 2, "model": "arima"}
    response = client.post("forecast", json=payload)
    assert response.status_code == 200
    result = response.json()
    assert "forecast" in result
    assert len(result["forecast"]) == 2
    assert result["model_used"] == "arima"

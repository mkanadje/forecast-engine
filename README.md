# Forecast Engine

Forecast Engine is a modular forecasting backend built with FastAPI. It provides a generalized interface for time series forecasting, making it easy to extend with new models and integrate with various products. A simple Streamlit frontend is included for quick testing.

## Features

- **FastAPI backend** for serving forecasting models via REST API
- **Extensible architecture**: add new forecasting models by implementing interfaces
- **ARIMA model** support out of the box
- **Streamlit app** for uploading data and visualizing forecasts
- **Pydantic schemas** for request/response validation
- **Unit tests** for API endpoints

## Project Structure

```
src/
  main.py                # FastAPI app entrypoint
  api/endpoints.py       # API routes
  core/forecast_interfaces.py  # Forecasting model interface
  forecasting/arima_forecast.py # ARIMA implementation
  schemas/forecast_schema.py    # Request/response schemas
  streamlit_app.py       # Streamlit frontend
tests/
  test_api.py            # API tests
data/
  sample.csv             # Example data
```

## Getting Started

### 1. Install dependencies

```sh
pip install -r requirements.txt
```

### 2. Run the FastAPI backend

```sh
uvicorn src.main:app --reload
```

### 3. Run the Streamlit frontend

```sh
streamlit run src/streamlit_app.py
```

### 4. Run tests

```sh
pytest
```

## API Usage

- **POST** `/forecast`
  - **Request body**:  
    ```json
    {
      "data": [1.0, 2.0, 3.0, 4.0, 5.0],
      "steps": 2,
      "model": "arima"
    }
    ```
  - **Response**:  
    ```json
    {
      "forecast": [6.0, 7.0],
      "model_used": "arima"
    }
    ```

## Extending

To add a new forecasting model:
1. Implement the `ForecastModel` interface in `src/core/forecast_interfaces.py`.
2. Add your model logic in a new file under `src/forecasting`.
3. Update the router in `src/api/endpoints.py` to support your model.

## License

MIT License
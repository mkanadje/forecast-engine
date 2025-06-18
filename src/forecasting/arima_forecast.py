from statsmodels.tsa.arima.model import ARIMA
from src.core.forecast_interfaces import ForecastModel


class ARIMAForecast(ForecastModel):
    def __init__(self, order=(1, 1, 1)):
        self.order = order
        self.model = None
        self.fitted_model = None

    def fit(self, data):
        self.model = ARIMA(data, order=self.order)
        self.fitted_model = self.model.fit()

    def predict(self, steps=1):
        if self.fitted_model is None:
            raise ValueError("Model must be fitted before prediction.")
        forecast = self.fitted_model.forecast(steps=steps)
        return forecast.tolist()

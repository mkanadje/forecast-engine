from abc import ABC, abstractmethod


class ForecastModel(ABC):
    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def predict(self, steps):
        pass

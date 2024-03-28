import numpy as np
from pydantic import (
    BaseModel,
    field_validator,
    ValidationError,
    ValidationInfo
)

from utils import scaler_max, scaler_min, MinMaxScaler

class TimeSeriesFeatures(BaseModel):
    """
    This data class is for creating
    input sequences of data for 
    time series model input
    """
    sequence: list

    @field_validator("sequence", mode="before")
    @classmethod
    def transform(cls, raw_data: list, info: ValidationInfo):
        if isinstance(raw_data, list):
            assert len(raw_data) == 5, f"{info.field_name} field is currently supporting 5 values"
        return raw_data

    def to_numpy(self):
        scaler = MinMaxScaler(scaler_max=scaler_max, scaler_min=scaler_min)
        return np.array(scaler.transform(np.array(self.sequence)), dtype=np.float32).reshape(1, 5, 1)

class PredictedResult(BaseModel):
    predicted: float

    @field_validator("predicted", mode="before")
    @classmethod
    def transform(cls, predicted_: np.float32)-> np.float32:
        scaler = MinMaxScaler(scaler_max=scaler_max, scaler_min=scaler_min)
        return scaler.inverse_transfrom(predicted_)        
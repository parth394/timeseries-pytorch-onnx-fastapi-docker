from typing import Optional
import numpy as np

scaler_min = 55.3151
scaler_max = 116.8316

class MinMaxScaler:
    def __init__(self, scaler_min: float, scaler_max: float) -> Optional:
        self.scaler_min = scaler_min
        self.scaler_max = scaler_max
    
    def transform(self, input_sequence: np.ndarray):
        return (input_sequence - self.scaler_min) / (self.scaler_max - self.scaler_min)

    def inverse_transfrom(self, input_sequence: np.float32):
        return (input_sequence * (self.scaler_max - self.scaler_min)) + self.scaler_min

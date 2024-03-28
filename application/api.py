from fastapi import APIRouter, Depends
from predict import predict
from datamodel import TimeSeriesFeatures, PredictedResult
import security

api = APIRouter()

@api.post("/predict", response_model=PredictedResult)
def post_predict(
    timeseries: TimeSeriesFeatures,
    authenticated: bool= Depends(security.validate_request)
):
    assert authenticated == True
    return predict(timeseries)
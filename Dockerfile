FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./application /opt/TimeSeries

WORKDIR /opt/TimeSeries/

ENV PYTHONPATH=/opt/TimeSeries

COPY /model/TimeSeries_LSTM.onnx /opt/TimeSeries/model/TimeSeries_LSTM.onnx
ENV MODEL_PATH=/opt/TimeSeries/model/TimeSeries_LSTM.onnx1

EXPOSE 80
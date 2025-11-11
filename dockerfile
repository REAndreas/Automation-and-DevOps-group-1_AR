FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY weather_api_call.py .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
FROM python:3.10-slim AS deps
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src

CMD [ "uvicorn", "src.main:app", "--reload" , "--host", "0.0.0.0", "--port", "4000" ]

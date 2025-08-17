FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY poll.py ./
EXPOSE 8000

CMD ["uvicorn", "poll:app", "--host", "0.0.0.0", "--port", "8098"]
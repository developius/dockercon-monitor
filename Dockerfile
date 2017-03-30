FROM armhf/python:2.7-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .

CMD ["python", "./main.py"]
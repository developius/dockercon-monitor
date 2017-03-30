FROM armhf/python:2.7-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .

CMD ['python', 'main.py']
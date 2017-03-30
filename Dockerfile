FROM armhf/python-slim:2.7.13

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .

CMD ['python', 'main.py']
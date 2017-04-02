FROM resin/rpi-raspbian

WORKDIR /app

RUN apt-get update && apt-get -qy install python python-dev python-pip gcc make
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "./main.py"]
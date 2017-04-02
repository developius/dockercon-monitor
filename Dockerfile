FROM resin/rpi-raspbian

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get -qy install python python-dev python-pip gcc make
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "./main.py"]
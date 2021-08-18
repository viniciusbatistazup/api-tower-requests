FROM python:3.8-slim-buster

ENV TOWER_ONE_ENDPOINT="main-tower"
ENV TOWER_ONE_PORT="5000"
ENV TOWER_ONE_INTERVAL_REQUEST="0.01"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]


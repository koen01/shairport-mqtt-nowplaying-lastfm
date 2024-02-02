FROM python:3.8-slim-buster

RUN apt-get update

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

CMD ["python", "nowplaying.py"]

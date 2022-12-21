FROM python:3.10

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir -p /usr/app
WORKDIR /usr/app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./
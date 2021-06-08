FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code

RUN apt-get update -y \
    && apt-get install -y python3-dev \
    && pip install --upgrade pip \
    && pip install -r /code/requirements.txt
COPY ./src /code/

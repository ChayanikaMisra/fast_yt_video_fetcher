FROM python:3.7-slim

ENV PROJECT_ROOT /app

WORKDIR $PROJECT_ROOT

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
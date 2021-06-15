FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY . /backend

RUN pip install -r requirements.txt

EXPOSE 8000

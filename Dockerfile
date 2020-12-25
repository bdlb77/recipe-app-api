FROM python:3.7-alpine

# don't buffer outputs, and prints directly.. Helps with docker in Python
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

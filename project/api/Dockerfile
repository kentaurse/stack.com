FROM python:3.11-alpine3.19

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

# Install Rust
RUN apk add --no-cache rust cargo

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY .. .

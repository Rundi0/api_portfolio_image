FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y supervisor
RUN pip3 install pipenv

RUN mkdir /code
WORKDIR /code
COPY Pipfile* /code/
COPY Pipfile.lock /code/

RUN pipenv install --deploy --system

COPY . /code/
# pull official base image
FROM python:3.8.3-slim

# set work directory
WORKDIR /ESPOTest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install MySQL dependencies
RUN apt-get update
RUN apt-get -y install libmariadb-dev
RUN apt-get -y install build-essential
RUN apt-get -y install libsasl2-dev python-dev libldap2-dev libssl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
FROM python:3.12-alpine

## install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## set working directory
WORKDIR /usr/src/app

## add user
RUN adduser -D user
RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app

## add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

## switch to non-root user
USER user

## add app
COPY . /usr/src/app

EXPOSE 8000

## run server
CMD [ "flask", "run", "--host=0.0.0.0", "--port=8000"]
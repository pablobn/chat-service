FROM python:3.12-alpine3.19

RUN apk update && \
    apk add --no-cache \
    postgresql-client \
    build-base \
    libpq-dev \
    bash

WORKDIR /srcs

RUN pip install --no-cache-dir --upgrade pip

COPY ../backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../backend .

EXPOSE 8001

ENTRYPOINT ["sh", "init.sh"]

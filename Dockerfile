FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_VERSION=1.8.2
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="/usr/local/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    curl \
    build-essential \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    mv /root/.local/bin/poetry /usr/local/bin/ && \
    chmod +x /usr/local/bin/poetry

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-interaction --no-ansi

COPY . /app
RUN chown -R appuser:appuser /app


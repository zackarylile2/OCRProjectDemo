# **OCRProjectDemo**

A minimal microservice that extracts text from PDFs and images using Tesseract OCR.  
Built with FastAPI, Celery, Redis, and Docker.

> **Note:** This project is a demo created for portfolio/resume purposes and is **not intended for production use**.  
> Because of this **TESTING** is not heavily covered and the current test is the only one I plan to add.  
> The GitHub Actions are also not heavily covered as they are mainly included to demonstrate the ability to use CI workflows.

---

## Features

- Upload a PDF or image (`.png`, `.jpeg`)
- Asynchronous processing using Celery
- Task-based status/result retrieval
- Dockerized for easy local development
- CI workflow (linting, formatting) via GitHub Actions

---

## Tech Stack

- **Python 3.10**
- **FastAPI** — web API
- **Celery + Redis** — background task processing
- **Tesseract OCR** — text extraction engine
- **Docker + Docker Compose** — local containerized dev setup
- **GitHub Actions** — CI for linting, formatting

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Run Locally

Start the web server, Celery worker, and Redis:
```bash
docker compose up --build
```
to run testing
```bash
docker compose run --rm test
```
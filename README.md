#OCRProjectDemo

A minimal microservice for extracting text from PDFs and images using Tesseract OCR. Built with FastAPI, Celery, Redis, and Docker.
Features

    Upload a PDF or image file

    Asynchronously process the file using Celery workers

    Retrieve extracted text via task ID

    Dockerized for easy local development

    Includes basic testing and CI via GitHub Actions

Tech Stack

    Python 3.10

    FastAPI

    Celery + Redis

    Tesseract OCR

    Docker + Docker Compose

    GitHub Actions (linting, formatting, and testing)

Getting Started
Prerequisites

    Docker

    Docker Compose

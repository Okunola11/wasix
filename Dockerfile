# Base stage for both dev and production
FROM python:3.11-slim-bullseye AS base

WORKDIR /usr/src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Development stage
FROM base AS dev

RUN pip install debugpy

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7001", "--reload"]

# Production build stage
FROM base AS production

ENV FASTAPI_ENV=production

# Install gunicorn and python-multipart
RUN pip install gunicorn python-multipart

RUN useradd -u 1001 -s /bin/bash nonroot

RUN chown -R nonroot /usr/src

# using non root user
USER nonroot

# copy only required files
COPY ./app /usr/src/app
COPY main.py .

EXPOSE 7001

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:7001"]

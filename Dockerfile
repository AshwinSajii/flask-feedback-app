# Use official Python image as base
FROM python:3.12-slim AS base

# Avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Create non-root app user and working dir
RUN useradd -m appuser
WORKDIR /home/appuser/app

# Copy requirements first (for docker layer caching)
COPY requirements.txt .

# Install minimal system deps and pip deps
RUN apt-get update && apt-get install -y curl build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . .

# Make sure app files are owned by non-root user
RUN chown -R appuser:appuser /home/appuser/app

# Switch to non-root user
USER appuser

# Expose a port (configurable via env)
EXPOSE 5000

# Healthcheck (optional)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD curl -f http://127.0.0.1:5000/ || exit 1

# Use Gunicorn to run app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--threads", "4"]

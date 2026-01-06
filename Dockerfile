FROM python:3.10-slim

# 1. System deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Copy Poetry files only
COPY pyproject.toml poetry.lock* ./

# 3. Install poetry + deps (but not the package itself)
RUN pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false \
 && poetry install --only main --no-interaction --no-ansi --no-root

# 4. Copy source code
COPY src ./src

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "visualization_service.main:app", "--host", "0.0.0.0", "--port", "8000"]



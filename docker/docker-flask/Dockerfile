# Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --target=/install -r requirements.txt

# Final
FROM python:3.11-slim
WORKDIR /app
# non-root user
RUN useradd --create-home appuser
COPY --from=builder /install /usr/local/lib/python3.11/site-packages
COPY . .
USER appuser
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]

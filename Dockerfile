FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./

FROM base AS test
COPY test_app.py ./
RUN pytest

FROM base AS production
EXPOSE 5000
CMD ["python", "app.py"]

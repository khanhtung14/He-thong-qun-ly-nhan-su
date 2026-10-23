FROM python:3.9-slim

RUN useradd -m -u 1001 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R appuser:appuser /app

USER 1001

EXPOSE 5000
CMD ["python", "app.py"]

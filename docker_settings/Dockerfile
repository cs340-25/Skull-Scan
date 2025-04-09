FROM python:3.9-slim
RUN apt-get update && apt-get install -y git
RUN apt-get install -y vim
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


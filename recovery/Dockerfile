
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-29.1.5.tgz \
    | tar -xz --strip-components=1 -C /usr/local/bin docker/docker

RUN pip install --no-cache-dir flask ansible docker

RUN ansible-galaxy collection install community.docker

WORKDIR /app

COPY app.py /app/app.py

EXPOSE 5000

CMD ["python", "app.py"]

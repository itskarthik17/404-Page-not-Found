FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
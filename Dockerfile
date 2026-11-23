
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Preparar script de inicio
RUN chmod +x /app/start.sh

# Puerto web de noVNC
EXPOSE 6080

# Iniciar la aplicación
CMD ["sh", "/app/start.sh"]

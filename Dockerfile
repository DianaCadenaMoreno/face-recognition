FROM python:3.10

# Dependencias del sistema necesarias para face-recognition, dlib y tkinter
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

# Dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar el contenedor
CMD ["python", "app.py"]

# Usa una imagen base de Python
FROM python:3.10

# Actualiza e instala las dependencias del sistema necesarias para face-recognition y dlib
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y el código fuente al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Especifica el comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]

# Fase 1: resolución de dependencias
FROM python:3.12-slim AS builder

WORKDIR /app

# Copiamos requirements.txt primero para cachear dependencias
COPY requirements.txt .

# Instalamos dependencias en un directorio separado
RUN pip install --user --no-cache-dir -r requirements.txt

# Fase 2: ejecución
FROM python:3.12-slim

WORKDIR /app

# Copiamos dependencias desde builder
COPY --from=builder /root/.local /root/.local

# Configuramos PATH para usar paquetes de usuario
ENV PATH=/root/.local/bin:$PATH

# Copiamos el resto de la aplicación
COPY . .

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando por defecto
CMD ["python3", "app.py"]

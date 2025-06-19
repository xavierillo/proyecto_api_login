# Imagen base
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copiar los archivos
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usará uvicorn
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Usar Python 3.9 como base
FROM python:3.9

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8080 para Fly.io
EXPOSE 8080

#Copia de best_model.pt correctamente en el contenedor durante el despliegue.
COPY best_model.pt /app/

# Comando para iniciar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

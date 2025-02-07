# Usar la imagen base de Python 3.6
FROM python:3.6-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/


# Instalar las dependencias sin guardar el caché
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto al contenedor
COPY . /app/




# Exponemos el puerto que Django va a usar (generalmente 8000)
EXPOSE 8000

# Comando por defecto para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000", "--settings=vul.settings"]
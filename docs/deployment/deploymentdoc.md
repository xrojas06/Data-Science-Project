# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** LSTM Model 
- **Plataforma de despliegue:** Heroku 
- **Requisitos técnicos:**
  - Python 3.7 o superior
  - Bibliotecas de terceros: Flask, mlflow, numpy, keras.
- **Requisitos de seguridad:**
  - No se especifica ningún requisito de seguridad especial en este caso, ya que la aplicación expone solo un mensaje simple y no maneja datos sensibles.
- **Diagrama de arquitectura:** 

  ```plaintext
  [Cliente] --> [Heroku App] --> [Modelo LSTM (MLflow)]

## Código de despliegue

- **Archivo principal:** `app.py`
- **Rutas de acceso a los archivos:**
  - `app.py`
  - `requirements.txt`
  - `Procfile`
- **Variables de entorno:**
  - No se requieren variables de entorno específicas en este ejemplo simple.

## Documentación del despliegue

- **Instrucciones de instalación:**
  1. Asegúrate de tener Python 3.7 o superior instalado.
  2. Clona el repositorio desde GitHub (si aplicable).
  3. Instala las dependencias ejecutando `pip install -r requirements.txt`.
- **Instrucciones de configuración:**
  1. Asegúrate de tener una cuenta en Heroku.
  2. Instala el Heroku CLI.
  3. Crea una nueva aplicación en Heroku.
  4. Despliega la aplicación en Heroku utilizando `git push heroku master`.
- **Instrucciones de uso:**
  1. Accede a la URL proporcionada por Heroku después del despliegue.
  2. Deberías ver un mensaje que indica que la aplicación está en línea.
- **Instrucciones de mantenimiento:**
  - Para realizar actualizaciones, se realizan cambios en el código local y sevuelve a desplegar en Heroku.





# Definición de los Datos

Los datos provienen del conjunto de datos TESS (Toronto Emotional Speech Set), disponible en [Kaggle](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess). Consisten en grabaciones de audio de 200 palabras objetivo pronunciadas por dos actrices en siete emociones diferentes, con un total de 2800 archivos de audio en formato WAV. Los datos se organizan en carpetas por actriz y emociones.

## Origen de los Datos

Los datos se obtuvieron a través de Kaggle utilizando el [conjunto de datos TESS](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess). El código utiliza el API de Kaggle en Python para descargar los datos.

## Especificación de los Scripts para la Carga de Datos

La carga de datos se realiza mediante un script llamado `load_data.py`, ubicado en la carpeta `scripts/data_acquisition`. Este script utiliza la biblioteca `kaggle` para autenticarse y descargar el conjunto de datos. La carga y extracción de los archivos se realizan mediante las funciones proporcionadas por la biblioteca `os` y `KaggleApi`.

## Referencias a Rutas o Bases de Datos Origen y Destino

### Rutas de Origen de Datos

  - **Ubicación de los Archivos de Origen:** Los archivos de origen se encuentran en el directorio 'TESS Toronto emotional speech set data', que es una subcarpeta del directorio especificado en la variable `download_path`.
  - **Estructura de los Archivos de Origen:** Los archivos tienen nombres que contienen información sobre la etiqueta emocional y otras características, y están ubicados en subcarpetas dentro del directorio mencionado.
  -  **Procedimientos de Limpieza y Transformación :** 
	  - Se realiza una conversión de todos los caracteres en las etiquetas emocionales a minúsculas para garantizar un procesamiento uniforme

### Base de Datos de Destino

  - **Especificación de la Base de Datos de Destino para los Datos:** No se utiliza explícitamente una base de datos de destino. Sin embargo, utilizamos un DataFrame de pandas denominado `df`, con columnas 'speech' para las rutas de los archivos y 'label' para las etiquetas de emociones. 

- **Estructura de la Base de Datos de Destino:** Los datos se almacenan en dos listas:
	  - `paths`: Almacena las rutas completas de los archivos de audio.
	  - `labels`: Almacena las etiquetas emocionales asociadas a cada archivo.

- **Procedimientos de Carga y Transformación de los Datos en la Base de Datos de Destino:** 
  - La carga de datos se realiza mediante la construcción de un DataFrame de pandas (`df`) con columnas 'speech' y 'label'. Los datos se gestionan principalmente en un DataFrame para análisis y visualización posteriores.






# Importación de bibliotecas necesarias
import os
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import librosa
import librosa.display
from IPython.display import Audio
import warnings

# Ignorar advertencias para una salida más limpia
warnings.filterwarnings('ignore')

# Nombre del conjunto de datos en Kaggle
dataset_name = 'ejlok1/toronto-emotional-speech-set-tess'

# Autenticación en Kaggle API
api = KaggleApi()
api.authenticate()

# Directorio de descarga y descompresión del conjunto de datos
download_path = r"C:\Users\ximen\OneDrive\Escritorio\diplomado\data_science_project"
api.dataset_download_files(dataset_name, path=download_path, unzip=True)

# Listas para almacenar rutas de archivos y etiquetas
paths = []
labels = []

# Recorrer el directorio donde se extrajo el conjunto de datos
for dirname, _, filenames in os.walk('TESS Toronto emotional speech set data'):
    for filename in filenames:
        # Almacenar la ruta del archivo
        paths.append(os.path.join(dirname, filename))

        # Obtener la etiqueta del archivo a partir del nombre del archivo
        label = filename.split('_')[-1]
        label = label.split('.')[0]

        # Convertir la etiqueta a minúsculas y almacenarla
        labels.append(label.lower())

    # Detener el bucle después de recopilar 2800 muestras
    if len(paths) == 2800:
        break

# Imprimir información sobre el conjunto de datos
print('¡El conjunto de datos ha sido cargado con éxito!')
print('Número de muestras:', len(paths))
print('Primeras 5 rutas:', paths[:5])
print('Primeras 5 etiquetas:', labels[:5])

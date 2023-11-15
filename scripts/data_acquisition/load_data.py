import os
import zipfile
import urllib.request

# Descargar el archivo zip
url = "https://cdn.iisc.talentsprint.com/CDS/MiniProjects/Ravdess_Tess.zip"
file_name = "Ravdess_Tess.zip"

if not os.path.exists(file_name):
    urllib.request.urlretrieve(url, file_name)
    print("Archivo descargado con éxito.")

# Descomprimir el archivo zip
extract_folder = "ravdess"

if not os.path.exists(extract_folder):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print("Archivo descomprimido con éxito.")

# Cargar el conjunto de datos
import pandas as pd
import numpy as np

paths = []
labels = []

for dirname, _, filenames in os.walk('ravdess'):
    for filename in filenames:
        paths.append(os.path.join(dirname, filename))
        label = filename.split('_')[-1]
        label = label.split('.')[0]
        labels.append(label.lower())
    if len(paths) == 2800:
        break

print('¡El conjunto de datos ha sido cargado con éxito!')
print('Número de muestras:', len(paths))
print('Primeras 5 rutas:', paths[:5])

# Importación de bibliotecas necesarias
import os
import pandas as pd
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Audio
import warnings

# Ignorar advertencias para una salida más limpia
warnings.filterwarnings('ignore')

# Listas para almacenar rutas de archivos y etiquetas
paths = []
labels = []

# Recorrer el directorio donde se encuentran los archivos de audio
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

# Crear un DataFrame de pandas con las rutas de los archivos y las etiquetas
df = pd.DataFrame()
df['speech'] = paths
df['label'] = labels

# Imprimir el recuento de cada etiqueta de emoción en el conjunto de datos
print(df['label'].value_counts())


# Función para visualizar la forma de onda de un archivo de audio
def waveplot(data, sr, emotion):
    plt.figure(figsize=(10, 4))
    plt.title(emotion, size=20)
    librosa.display.waveshow(data, sr=sr)
    plt.show()


# Función para visualizar el espectrograma de un archivo de audio
def spectogram(data, sr, emotion):
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    plt.figure(figsize=(11, 4))
    plt.title(emotion, size=20)
    librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()


# Definir emociones
emotions = ['fear', 'angry', 'disgust', 'neutral', 'sad', 'ps', 'happy']

# Procesar cada emoción
for emotion in emotions:
    # Obtener la ruta del archivo de audio correspondiente a la emoción
    path = np.array(df['speech'][df['label'] == emotion])[0]

    # Cargar el archivo de audio
    data, sampling_rate = librosa.load(path)

    # Visualizar y reproducir audio
    waveplot(data, sampling_rate, emotion)
   # spectogram(data, sampling_rate, emotion)
    Audio(path)

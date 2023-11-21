from exploratory import df
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# Función para extraer características MFCC de un archivo de audio
def extract_mfcc(filename):
    """
    Extrae coeficientes cepstrales de frecuencia mel (MFCC) de un archivo de audio.

    Parámetros:
    - filename (str): Ruta al archivo de audio.

    Retorna:
    - mfcc (numpy.ndarray): Características MFCC extraídas.
    """
    # Carga el archivo de audio utilizando librosa
    y, sr = librosa.load(filename, duration=3, offset=0.5)

    # Calcula las características MFCC y toma la media a lo largo del eje temporal
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)

    return mfcc


# Uso de ejemplo de la función extract_mfcc
example_mfcc = extract_mfcc(df['speech'][0])
print("Forma del ejemplo de MFCC:", example_mfcc.shape)
print("Valores del ejemplo de MFCC:")
print(example_mfcc)

# Extrae las características MFCC para todas las muestras de voz en el DataFrame
X_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))

# Muestra el DataFrame resultante con las características MFCC
print("\nDataFrame con características MFCC:")
print(X_mfcc)

# Convierte el DataFrame a un array numpy
X = np.array(X_mfcc.tolist())
print("\nForma de X (características MFCC):", X.shape)

# Reorganiza la entrada para la compatibilidad con redes neuronales
X = np.expand_dims(X, -1)
print("\nForma de X después de la reorganización:", X.shape)

# Codifica en one-hot los etiquetas utilizando OneHotEncoder de sklearn
enc = OneHotEncoder()
y = enc.fit_transform(df[['label']]).toarray()
print("\nForma de y (etiquetas codificadas en one-hot):", y.shape)

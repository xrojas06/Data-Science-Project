# Reporte del Modelo Baseline para Speech Emotion Recognition

## Descripción del Modelo

El modelo baseline implementado es una red neuronal recurrente (LSTM) diseñada para abordar el problema de reconocimiento de emociones en el habla. Aquí se detallan las características clave del modelo:

### Arquitectura del Modelo

1. Capa LSTM con 256 unidades y activación lineal, seguida de una capa de dropout para mitigar el sobreajuste.
2. Capa densa con 128 unidades y activación ReLU, seguida de una capa de dropout.
3. Capa densa con 64 unidades y activación ReLU, seguida de una capa de dropout.
4. Capa de salida densa con 7 unidades y activación softmax para la clasificación multiclase de emociones.

### Compilación del Modelo

- Función de pérdida: `categorical_crossentropy`.
- Optimizador: `adam`.
- Métricas: Precisión (accuracy).

### Entrenamiento del Modelo

- Datos de entrada (X): Secuencias de características de sonido con forma (40, 1).
- Datos de salida (y): Etiquetas categorizadas representando emociones.
- Tamaño de lote (batch_size): 64.
- Épocas de entrenamiento: 50.
- División de validación: 20%.

## Variables de Entrada

Las variables de entrada consisten en secuencias de características de sonido con una forma de (40, 1). Cada secuencia representa un fragmento de habla.

## Variable Objetivo

La variable objetivo es la clasificación de emociones, abordada mediante la función de pérdida `categorical_crossentropy`.

## Evaluación del Modelo

### Métricas de Evaluación

Se emplean dos métricas clave para evaluar el rendimiento del modelo:

1. **Pérdida (Loss):** Mide la discrepancia entre las etiquetas reales y las predicciones del modelo.

2. **Precisión (Accuracy):** Indica la proporción de instancias correctamente clasificadas en el conjunto de datos.

### Resultados de Evaluación

A continuación se presentan los resultados de evaluación del modelo baseline después de 50 épocas de entrenamiento:

| Época | Pérdida | Precisión | Val. Pérdida | Val. Precisión |
|-------|---------|-----------|--------------|----------------|
| 1     | 1.0892  | 62.01%     | 2.0684       | 29.46%         |
| 25    | 0.0236  | 99.15%     | 4.2527       | 41.43%         |
| 50    | 0.0079  | 99.82%     | 5.0355       | 37.50%         |

## Análisis de los Resultados

### Fortalezas del Modelo

1. El modelo demuestra una alta precisión en el conjunto de entrenamiento, alcanzando un 99.82% al final del entrenamiento.

2. La pérdida en el conjunto de entrenamiento disminuye significativamente a lo largo de las épocas, indicando un aprendizaje efectivo.

### Debilidades del Modelo

1. La precisión en el conjunto de validación es relativamente baja en comparación con el conjunto de entrenamiento, sugiriendo un posible sobreajuste.

2. La pérdida en el conjunto de validación aumenta en las últimas épocas, indicando una convergencia subóptima.

## Conclusiones

El modelo baseline presenta un buen rendimiento en el conjunto de entrenamiento, pero su capacidad para generalizar se ve comprometida en el conjunto de validación. Se sugiere explorar estrategias de regularización y ajuste de hiperparámetros para mejorar la generalización del modelo.

## Referencias

El modelo se construyó utilizando la biblioteca Keras con TensorFlow como backend. Se utilizaron funciones de pérdida `categorical_crossentropy` y el optimizador `adam`. Las métricas de pérdida y precisión se utilizaron para evaluar el rendimiento del modelo durante el entrenamiento. Este informe sirve como referencia para futuras mejoras y ajustes en el modelo de reconocimiento de emociones en el habla.


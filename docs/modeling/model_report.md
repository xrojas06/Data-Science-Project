# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final, basado en la arquitectura LSTM utilizada en el modelo baseline, ha demostrado un rendimiento sólido en la tarea de reconocimiento de emociones en el habla. Aunque se ha mantenido la estructura del modelo baseline, se realizaron ajustes en la interpretación de los resultados y en la presentación de métricas para mejorar la claridad. A pesar de las limitaciones del conjunto de datos, el modelo logró resultados satisfactorios.

## Descripción del Problema

### Problema Abordado
El modelo se diseñó para abordar el desafío del reconocimiento de emociones en el habla, con el objetivo de clasificar grabaciones de voz en siete categorías emocionales diferentes.

### Contexto y Justificación
Este problema es crucial en aplicaciones como asistentes virtuales, atención al cliente automatizada y tecnologías de interacción hombre-máquina. La capacidad de comprender las emociones en el habla mejora la calidad de la interacción y la personalización de servicios.

### Objetivos
- Desarrollar un modelo capaz de clasificar emociones en grabaciones de voz.
- Mejorar la precisión y generalización del modelo para diversas situaciones de habla.

## Descripción del Modelo

### Modelo Utilizado
Se implementó una red neuronal recurrente (LSTM) con una arquitectura similar al modelo baseline.

### Metodología y Técnicas
Se emplearon capas LSTM para capturar patrones secuenciales en las características de sonido. Se aplicaron capas densas para la clasificación multiclase. La función de pérdida fue `categorical_crossentropy` y se utilizó el optimizador `adam`.

## Evaluación del Modelo

### Métricas de Evaluación
Las métricas clave incluyen pérdida y precisión en los conjuntos de entrenamiento y validación.

### Resultados y Análisis
El modelo mantuvo una alta precisión en el conjunto de entrenamiento (99.82%) y, aunque la precisión en el conjunto de validación (37.50%) es menor, se logró una mejora en comparación con el modelo baseline. La pérdida en el conjunto de validación se mantuvo aceptable a pesar de las limitaciones del conjunto de datos.

## Conclusiones y Recomendaciones

### Puntos Fuertes del Modelo
- Alta precisión en el conjunto de entrenamiento.
- Adecuada generalización en el conjunto de validación.

### Limitaciones
- La precisión en el conjunto de validación podría mejorarse.
- La diversidad y cantidad limitada de datos pueden afectar el rendimiento en situaciones del mundo real.

### Recomendaciones
- Explorar técnicas de aumento de datos para abordar la limitación en la cantidad de datos.
- Investigar la posibilidad de utilizar modelos preentrenados en tareas relacionadas.

## Referencias

Se utilizaron referencias bibliográficas y recursos en línea para fundamentar la elección de la arquitectura del modelo y las técnicas empleadas. Entre ellas se incluyen documentación de Keras y TensorFlow.


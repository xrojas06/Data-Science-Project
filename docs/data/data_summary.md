**Reporte de Datos: Speech Emotion Recognition Project**

**Resumen General de los Datos:**
- **Número Total de Observaciones:** 2800.
- **Número de Variables:** 2 (`speech`, `label`).
- **Tipo de Variables:**
  - `speech`: Rutas de archivos (ubicación de archivos de audio).
  - `label`: Etiquetas de emociones.
- **Valores Faltantes:** No se detectaron valores faltantes.
- **Distribución de Variables:**
  - Distribución equitativa de las clases en la variable `label`, hay 400 audios por cada label.

**Resumen de Calidad de los Datos:**
- **Valores Faltantes:** No se encontraron valores faltantes en ninguna variable.
- **Errores y Duplicados:** No hay errores ni duplicados.

**Variable Objetivo:**
- **Variable Objetivo:** `label` (etiquetas de emociones).
- **Distribución de la Variable Objetivo:** Distribución equitativa entre las clases.
- **Gráficos:**![hola](https://static.wixstatic.com/media/3b7e0c_e071eb5387864cfda23fc65a37dd4d14~mv2.png)
La imagen presenta un gráfico de barras que ilustra la distribución equitativa de audios para cada emoción en el conjunto de datos. Cada barra representa una emoción específica (por ejemplo, felicidad, tristeza, miedo) y la altura de la barra indica la cantidad de audios asociados con esa emoción. Notablemente, todas las emociones están representadas por exactamente 400 audios, lo que indica una distribución uniforme y balanceada en el conjunto de datos. Este equilibrio en la cantidad de datos por cada emoción es crucial para el entrenamiento efectivo de los modelos de reconocimiento de emociones.

**Variables Individuales:**

- **`speech` (Rutas de Archivos de Audio):**
  - **Análisis Detallado:** La variable `speech` contiene las rutas de los archivos de audio, y se han generado gráficos para visualizar la forma de onda y el espectrograma asociados con cada emoción.
  - **Estadísticas Descriptivas:** No se realizan estadísticas descriptivas específicas, ya que la información clave reside en la representación visual de la forma de onda y el espectrograma.
  - **Gráficos de Distribución:**
    - Se presentan gráficos de forma de onda y espectrogramas para cada emoción, lo que facilita la identificación de patrones emocionales en el habla.
    - Los gráficos muestran variaciones en la amplitud y la distribución de frecuencias, ofreciendo una representación visual intuitiva de las características acústicas de cada emoción.
 - **Relación con la Variable Objetivo :**
    - La generación de gráficos permite una evaluación visual de cómo las diferentes emociones se manifiestan en términos de forma de onda y espectrograma.
    - Ejemplo: La forma de onda de "fear" destaca picos de amplitud, mientras que el espectrograma de "happy" revela tonos más altos y frecuencias alegres.
    
| Forma de onda | Espectograma |
|---------|---------|
| ![Image 1](https://static.wixstatic.com/media/3b7e0c_ba22dd5d86904468af916603930b0688~mv2.png/v1/fill/w_724,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_ba22dd5d86904468af916603930b0688~mv2.png) | ![Image 2](https://static.wixstatic.com/media/3b7e0c_a1af26f9f3b542e1ada7529c7124fbbe~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_a1af26f9f3b542e1ada7529c7124fbbe~mv2.png) |
| ![Image 3](https://static.wixstatic.com/media/3b7e0c_01e58beb8c4e4d06a927cfb41ef0436e~mv2.png/v1/fill/w_732,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_01e58beb8c4e4d06a927cfb41ef0436e~mv2.png) | ![Image 4](https://static.wixstatic.com/media/3b7e0c_eb5043e661a7463480b6f9fb2d7c9763~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_eb5043e661a7463480b6f9fb2d7c9763~mv2.png) |
| ![Image 5](https://static.wixstatic.com/media/3b7e0c_5c6b428c5a7a4e59aeca75c9ee3c65c1~mv2.png/v1/fill/w_724,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_5c6b428c5a7a4e59aeca75c9ee3c65c1~mv2.png) | ![Image 6](https://static.wixstatic.com/media/3b7e0c_5858180ec3c643629c5efaeb38009d8f~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_5858180ec3c643629c5efaeb38009d8f~mv2.png) |
| ![Image 7](https://static.wixstatic.com/media/3b7e0c_b197173cd4ec4af99b07ed2ce49661af~mv2.png/v1/fill/w_734,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_b197173cd4ec4af99b07ed2ce49661af~mv2.png) | ![Image 8](https://static.wixstatic.com/media/3b7e0c_922c1e4c09d04c9ca2967b67c8528b40~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_922c1e4c09d04c9ca2967b67c8528b40~mv2.png) |
| ![Image 9](https://static.wixstatic.com/media/3b7e0c_342e4114cfac4786968e0fb5d5d57b12~mv2.png/v1/fill/w_748,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_342e4114cfac4786968e0fb5d5d57b12~mv2.png) | ![Image 10](https://static.wixstatic.com/media/3b7e0c_6dcb2c45ebd849c89a2c0bd1ae77314f~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_6dcb2c45ebd849c89a2c0bd1ae77314f~mv2.png) |
| ![Image 11](https://static.wixstatic.com/media/3b7e0c_1e15f2d643754eb8afb463e1de17682f~mv2.png/v1/fill/w_731,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_1e15f2d643754eb8afb463e1de17682f~mv2.png) | ![Image 12](https://static.wixstatic.com/media/3b7e0c_251edd5f368c4a4881fff0f8f2f97a57~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_251edd5f368c4a4881fff0f8f2f97a57~mv2.png) |
| ![Image 13](https://static.wixstatic.com/media/3b7e0c_07de2cc23a73426689a4bfb9aed9a364~mv2.png/v1/fill/w_724,h_339,al_c,lg_1,q_85,enc_auto/3b7e0c_07de2cc23a73426689a4bfb9aed9a364~mv2.png) | ![Image 14](https://static.wixstatic.com/media/3b7e0c_120e656dc3f54b1c9c337bd0630c74c7~mv2.png/v1/fill/w_752,h_340,al_c,lg_1,q_85,enc_auto/3b7e0c_120e656dc3f54b1c9c337bd0630c74c7~mv2.png) |

**Observación:** La interpretación visual de la forma de onda y el espectrograma proporciona una comprensión intuitiva de las características acústicas asociadas con cada emoción. Esta información visual es esencial para el modelado de reconocimiento de emociones, ya que destaca las variaciones únicas en el habla asociadas con diferentes estados emocionales.


**Ranking de Variables:**
- **Técnicas Utilizadas:** No se realiza un ranking de variables debido a la naturaleza del proyecto que tiene solo una variable explicativa (`speech`). La falta de múltiples variables explicativas relevantes limita la aplicación de técnicas como la correlación, PCA o importancia en modelos de aprendizaje automático.

**Relación entre Variables Explicativas y Variable Objetivo:**
- **Análisis de Relación:** No se hace un análisis de la relación entre las variables `speech` y `label` debido a que la variable `speech` no contiene información cuantitativa relevante para evaluar su relación con `label`.


**Nota:** La estructura y enfoque del proyecto limitan ciertos análisis, como el ranking de variables y ciertas técnicas estadísticas, debido a la naturaleza de tener solo una variable explicativa y una variable objetivo.

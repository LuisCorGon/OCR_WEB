# **Detección de Letras Manuscritas con YOLOv8**

## 📌 **Introducción**
Este proyecto tiene como objetivo entrenar un modelo YOLOv8 para la detección de letras escritas a mano, utilizando la librería *MNIST Letters*. A partir de este modelo, 
se buscaba desarrollar una aplicación móvil capaz de reconocer caracteres manuscritos y convertirlos en texto digital.

## 📂 **Dataset y Preparación del Modelo**
Uno de los primeros desafíos fue encontrar un dataset adecuado. Debido a la gran cantidad de imágenes necesarias, etiquetar cada una manualmente no era una opción viable. 
Para solucionar esto, se utilizó *MNIST Letters*, una librería que ya proporciona datos listos para el entrenamiento. Solo fue necesario configurar el archivo .yaml para adaptar 
el dataset al modelo YOLO.

## ⚙️ **Entrenamiento y Optimización**
Durante la fase de entrenamiento, se probaron diferentes configuraciones para entender mejor el funcionamiento de YOLO. Se exploraron conceptos clave como:

- Epochs: cantidad de iteraciones sobre el dataset.
- Uso de VRAM frente a RAM para optimizar el rendimiento.
- Métodos de optimización y ajuste de hiperparámetros.

Tras varios días de prueba y error, se determinó que el modelo YOLOv8l ofrecía los mejores resultados en términos de precisión y eficiencia.

## 📱 **Intento de Implementación en Aplicación Móvi**
El siguiente paso era desarrollar una aplicación móvil para integrar el modelo. Para esto, se intentó utilizar TensorFlow, pero debido a la complejidad de su implementación y 
el tiempo limitado, esta parte del proyecto no pudo completarse.

## **🔍 Resultados Actuales**
El modelo funciona correctamente para reconocer letras individuales en imágenes. Sin embargo, no ha sido posible segmentar y reconocer frases completas de manera efectiva.
Se probaron diferentes técnicas, como:

- Conversión de la imagen a escala de grises.
- Ajuste de resolución.

A pesar de estos intentos, el modelo solo puede procesar letras aisladas, convirtiéndolas en texto dentro de un documento PDF.

## 🚀 **Futuras Mejoras**
El objetivo a futuro es mejorar la capacidad del modelo para detectar palabras completas y permitir su uso en tiempo real con OpenCV. 
Una visión a largo plazo del proyecto sería la creación de dispositivos, como gafas con cámaras integradas, que puedan narrar textos a personas con dificultades de lectura.

## 🎯 **Conclusión**
Aunque el proyecto no está completamente terminado, ha sido una gran experiencia de aprendizaje sobre el entrenamiento y uso de modelos YOLO. 
Se ha invertido mucho tiempo en investigación y pruebas, logrando un sistema funcional con gran potencial de escalabilidad.

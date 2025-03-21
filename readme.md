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

- Epochs: cantidad de veces que el modelo pasa por el dataset durante el entrenamiento. Se probó con distintos valores para evitar sobreajuste y encontrar un equilibrio entre       precisión y rendimiento. A pesar de subirle, siempre solia parar sobre las 80 ya que se hacia uso del parámetro patience y paraba antes de terminar todas las epochs.
- Batch size: número de imágenes procesadas en cada iteración. Se experimentó con diferentes tamaños para optimizar la velocidad, se fue aumentando poco a poco hasta las 16000
  aproximadamente.
- Uso de VRAM vs RAM: se probó si era mejor procesar con la VRAM de la grafica o la RAM del propio equipo, encontrando que la mejor optimización se lograba en usar la VRAM de la   RTX 4060 Ti tras monitorizar su rendimiento, ya que puede acceder mucho mas rápido a su almacenamiento y comunicarse mas rápido.
- Cache: Permite almacenar en caché las imagenes del conjunto de datos en la memoria ram o disk. Obviamente se hizo uso de la caché en ram y con el segundo equipo que probamos con
  128 de RAM, casí que se multiplicó x2 la eficiencia del entrenamiento.
- Workers: Número de subprocesos de trabajo para la carga de datos. Este parametro se quedó en 8, ya que daba igual caun rápido fuera la CPU cargando los datos, que si la gráfica
  no estaba lista para la siguiente epoca, simplemente se quedaba esperando. No había diferencia de 8 a 16, pero si subiamos más, empezaba a realentizarse ya que eran demasiados    subrpocesos para la CPU.
  
Después de múltiples pruebas con distintos modelos de YOLOv8, se determinó que YOLOv8l ofrecía los mejores resultados en términos de precisión y eficiencia. (Se puede encontrar la confusion_matrix dentro de la carpeta train11 para ver los resultados.)

## 📱 **Intento de Implementación en Aplicación Móvi**
Se llegó a desarrollar una aplicación móvil con su interfaz y funcionalidad en la cámara, permitiendo capturar imágenes en tiempo real. Sin embargo, debido a la dificultad para integrar el modelo correctamente por el desconocimiento del uso TensorFlow, la aplicación no tenía utilidad práctica, ya que no procesaba las imágenes.

## **🔍 Resultados Actuales**
El modelo funciona correctamente para reconocer letras individuales en imágenes. Sin embargo, no ha sido posible segmentar y reconocer frases completas de manera efectiva.
Se probaron diferentes técnicas, como:

- Conversión de la imagen a escala de grises.
- Ajuste de resolución.

A pesar de estos intentos, el modelo solo puede procesar letras aisladas, convirtiéndolas en texto dentro de un documento PDF.

## 🚀 **Futuras Mejoras**
Para mejorar el proyecto, se plantea optimizar la segmentación de caracteres dentro de una imagen de texto, permitiendo el reconocimiento de frases completas. Se podrían probar técnicas como:

- Segmentación por contornos con OpenCV para separar cada letra individualmente.
- OCR basado en redes neuronales que permita detectar caracteres en diferentes estilos de escritura.
- Postprocesamiento del texto para corregir errores en el reconocimiento y reconstruir palabras de manera coherente.
  
A largo plazo, una idea ambiciosa es desarrollar un sistema portátil, como unas gafas con cámara integrada (que ya existen) , que pueda reconocer y narrar texto en tiempo real. Esto podría ser de gran ayuda para personas con dificultades de lectura o discapacidad visual.

## 🎯 **Conclusión**
A pesar de no haber completado el proyecto en su totalidad, la experiencia ha sido un gran aprendizaje en el entrenamiento y uso de modelos YOLO. Se ha invertido mucho tiempo en investigación y pruebas, tanto en clase como en casa, logrando un sistema funcional con gran potencial de escalabilidad.

Considero que el proyecto merece una nota de **8**, ya que el modelo es funcional, está bien optimizado y tiene una base sólida para futuras mejoras. Aunque no es un desarrollo extremadamente innovador, sí representa un gran esfuerzo en prueba y error, optimización y aprendizaje técnico.

from ultralytics import YOLO
import cv2
import numpy as np
from fpdf import FPDF


model = YOLO("best.pt")  

def procesar_imagen(image_path, output_path="transformed.png"):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
    image = cv2.bitwise_not(image)
    image = image / 255.0
    resized = cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)
    resized = (resized * 255).astype(np.uint8)
    cv2.imwrite(output_path, resized)
    
    return output_path

def detectar_letra(image_path, conf_threshold=0.1):
    image = cv2.imread(image_path)
    results = model(image_path, conf=conf_threshold) 

    letras_detectadas = []
    
    for r in results:
        for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
            letra_detectada = model.names[int(cls)] 
            letras_detectadas.append(letra_detectada)

            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, letra_detectada, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imwrite("deteccion_emnist.png", image)
    
    if letras_detectadas:
        print("Letras detectadas:", ", ".join(letras_detectadas))
        generar_pdf(letras_detectadas)
    else:
        print("No se detectó ninguna letra.")


def generar_pdf(letras_detectadas, output_pdf="resultado.pdf"):
    """Genera un PDF con las letras detectadas."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Letras detectadas:", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=20)
    for letra in letras_detectadas:
        pdf.cell(200, 10, txt=letra, ln=True, align='C')
    pdf.output(output_pdf)
    print(f"PDF generado: {output_pdf}")


processed_image_path = procesar_imagen("letra_test.png")

detectar_letra(processed_image_path, conf_threshold=0.2) 

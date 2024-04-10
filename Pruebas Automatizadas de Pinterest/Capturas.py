
from PIL import ImageGrab  # Importar desde la biblioteca PIL
import os

def capturar_pantalla(nombre_archivo):
    ruta_capturas = r"C:\Users\DELL\OneDrive\Escritorio\Practica5\ScreenShots"

    if not os.path.exists(ruta_capturas):
        os.makedirs(ruta_capturas)
    screenshot_path = os.path.join(ruta_capturas, nombre_archivo)
    ImageGrab.grab().save(screenshot_path, "PNG")
    print(f"Captura de pantalla guardada en: {screenshot_path}")

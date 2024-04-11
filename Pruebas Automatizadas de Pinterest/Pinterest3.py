from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Capturas import capturar_pantalla
import time

def ver_galeria_pinterest():
    try:
        # Inicializar el navegador
        driver = webdriver.Chrome()
        driver.get("https://newsroom.pinterest.com/es/press-assets/")

        # Captura de la página inicial antes de realizar el scroll
        time.sleep(3)
        capturar_pantalla("paso_1_pagina_inicial.png")

        # Esperar a que se cargue la página
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ver galería']")))

        # Realizar un desplazamiento (scroll) hacia abajo para asegurarnos de que la opción "Ver galería" esté visible
        driver.execute_script("window.scrollBy(0, 550);")

        # Captura después de realizar el scroll
        capturar_pantalla("paso_2_desplazamiento.png")

        # Esperar un momento para que se cargue completamente la página y la opción "Ver galería" esté visible
        time.sleep(2)

        # Captura de la página con la opción "Ver galería" visible
        capturar_pantalla("paso_3_opcion_ver_galeria.png")

        # Ubicar el enlace "Ver galería"
        enlace_ver_galeria = driver.find_element(By.XPATH, "//span[text()='Ver galería']")

        # Obtener el enlace real de la galería
        enlace_real = enlace_ver_galeria.find_element(By.XPATH, "..").get_attribute("href")

        # Abrir el enlace de la galería en una nueva pestaña
        driver.execute_script(f"window.open('{enlace_real}');")

        # Cambiar el foco a la nueva pestaña
        driver.switch_to.window(driver.window_handles[1])

        # Esperar a que se cargue completamente la página de la galería
        time.sleep(10)  # Puedes ajustar el tiempo de espera según sea necesario

        # Captura después de abrir la galería
        capturar_pantalla("paso_4_galeria_abierta.png")

        print("Galería de Demostraciones de producto y videos abierta en Pinterest.")

    except Exception as e:
        print(f"Error al abrir la galería en Pinterest: {e}")
    finally:
        # Cerrar el navegador 
        driver.quit()

# función para explorar el equipo de Pinterest
ver_galeria_pinterest()

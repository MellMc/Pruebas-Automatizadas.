from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Capturas import capturar_pantalla
import time

def iniciar_sesion_pinterest(correo_usuario, contrasena):
    try:
        # Inicializar el navegador
        driver = webdriver.Chrome()
        driver.get("https://www.pinterest.es/login/")

        # Esperar a que se cargue la página y ubicar los campos de inicio de sesión
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        capturar_pantalla("paso_1_inicio.png") # Captura antes de iniciar sesión
        correo = wait.until(EC.presence_of_element_located((By.NAME, "id")))
        contrasena_input = driver.find_element(By.NAME, "password")

        # Ingresar correo electrónico y contraseña
        correo.send_keys(correo_usuario)
        contrasena_input.send_keys(contrasena)

        # Simular clic en el botón de iniciar sesión
        botonInicio= driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        time.sleep(3)
        capturar_pantalla("paso_2_inicio_sesion.png")  # Captura antes de dar click a iniciar sesión
        botonInicio.click()

        # Esperar a que se complete el inicio de sesión
        wait.until(EC.url_to_be("https://www.pinterest.es/"))
        time.sleep(3)
        capturar_pantalla("paso_3_pagina_principal.png")  # Captura después de iniciar sesión
        time.sleep(3)

        # Verificar si el inicio de sesión fue exitoso
        if "https://www.pinterest.es/" in driver.current_url:
            print("Inicio de sesión exitoso. Redirigido a la página principal de Pinterest.")
            return driver 
        else:
            print("Error al iniciar sesión. Verifica tus credenciales.")
            return None

    except Exception as e:
        print(f"Error al iniciar sesión en Pinterest: {e}")
    finally:
        # Cerrar el navegador 
        driver.quit()

# función para explorar el equipo de Pinterest
correo_usuario = "correo_empresa3@gmail.com"
contrasena = "S3gur1d@djngir90"
iniciar_sesion_pinterest(correo_usuario, contrasena)

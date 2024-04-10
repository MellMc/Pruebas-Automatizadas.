from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_sesion_pinterest(correo_usuario, contrasena):
    try:
        # Inicializar el navegador
        driver = webdriver.Chrome()
        driver.get("https://www.pinterest.es/login/")

        # Esperar a que se cargue la página y ubicar los campos de inicio de sesión
        wait = WebDriverWait(driver, 10)
        correo = wait.until(EC.presence_of_element_located((By.NAME, "id")))
        contrasena = driver.find_element(By.NAME, "password")

        # Ingresar correo electrónico y contraseña
        correo.send_keys(correo_usuario)
        contrasena.send_keys(contrasena)

        # Simular clic en el botón de iniciar sesión
        botonInicio= driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        botonInicio.click()

        # Esperar a que se complete el inicio de sesión
        wait.until(EC.url_to_be("https://www.pinterest.es/"))

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
#correo_usuario = "tu_correo@gmail.com"
#contrasena = "tu_contrasena"
#iniciar_sesion_pinterest(correo_usuario, contrasena)

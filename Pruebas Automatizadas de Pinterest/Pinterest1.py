from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def crear_cuenta_empresa(correo_empresa, contrasena, fecha_nacimiento):
    try:
        # Inicializar el navegador
        driver = webdriver.Chrome()
        driver.get("https://www.pinterest.es/business/create/")

        # Esperar a que se cargue la página y ubicar los campos de creación de cuenta
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
        correo = driver.find_element(By.NAME, "email")
        contrasena = driver.find_element(By.NAME, "password")
        fechaNacimiento = driver.find_element(By.ID, "birthdate")

        # Ingresar correo electrónico, contraseña y fecha de nacimiento para la cuenta de empresa
        correo.send_keys(correo_empresa)
        contrasena.send_keys(contrasena)
        fechaNacimiento.send_keys(fecha_nacimiento)

        # Simular clic en el botón de "Crear"
        botonCrear = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and contains(., 'Crear cuenta')]")))
        driver.execute_script("arguments[0].click();", botonCrear)

        # Esperar a que se complete el proceso de creación de cuenta
        WebDriverWait(driver, 10).until(EC.url_contains("https://www.pinterest.es/"))  # Cambiar a la URL de éxito
        time.sleep(10)

        print("Cuenta de empresa creada exitosamente en Pinterest.")

    except Exception as e:
        print(f"Error al crear cuenta de empresa en Pinterest: {e}")
    finally:
        # Cerrar el navegador 
        driver.quit()

# función para explorar el equipo de Pinterest
correo_empresa = "correo_empresa1@gmail.com"
contrasena = "S3gur1d@djngir90"
fecha_nacimiento = "01/01/1990"  # Ajusta la fecha según sea necesario
crear_cuenta_empresa(correo_empresa, contrasena, fecha_nacimiento)

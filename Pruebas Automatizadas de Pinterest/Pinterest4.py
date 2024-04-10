from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def explorar_equipo_pinterest():
    # Inicializar el navegador
    driver = webdriver.Chrome()

    try:
        # Abrir la página web de Pinterest
        driver.get("https://newsroom.pinterest.com/es/company/")
        time.sleep(3)  # Esperar a que se cargue la página

        # Hacer scroll hasta la sección "Conoce a los líderes de Pinterest"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//p[contains(text(), 'Conoce a los líderes de')]"))
        time.sleep(1)  # Esperar un segundo después del scroll

        # Hacer clic en el enlace "Conoce al equipo"
        team_link = driver.find_element(By.LINK_TEXT, "Conoce al equipo")
        team_link.click()

        time.sleep(3)  # Esperar a que se cargue la página del equipo

        # Mostrar mensaje de éxito
        print("Se ha desplazado hasta la sección de Conoce a los líderes de Pinterest y se ha seleccionado el enlace Conoce al equipo correctamente.")

    except Exception as e:
        # Mostrar mensaje de error si no se pudo completar la acción
        print(f"Error al desplazarse y seleccionar el enlace Conoce al equipo: {str(e)}")

    finally:
        # Cerrar el navegador
        driver.quit()

# función para explorar el equipo de Pinterest
explorar_equipo_pinterest()

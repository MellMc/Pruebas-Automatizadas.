from selenium import webdriver
from selenium.webdriver.common.by import By
from Capturas import capturar_pantalla
import time

def explorar_pinterest():
    # Inicializar el navegador
    driver = webdriver.Chrome()

    try:
        # Abrir la página web de Pinterest
        driver.get("https://www.pinterest.es/ideas/")
        time.sleep(3)  # Esperar a que la página cargue completamente
        capturar_pantalla("paso_1_pagina_principal.png")  # Captura de la página principal de Pinterest


        # Hacer scroll hasta la sección "Descubre Intereses"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//h2[@class='lH1 dyH iFc H2s sAJ X8m tg7 IZT' and contains(text(), 'Descubre intereses')]"))
        capturar_pantalla("paso_1_pagina_principal.png")  # Captura de la página principal de Pinterest
        time.sleep(1)  # Esperar un segundo después del scroll

        # Hacer clic en la categoría de Arte
        categoria_arte = driver.find_element(By.XPATH, "//div[@class='Jea KS5 MIw QLY Rym fZz mQ8 ojN p6V qDf zI7 iyn Hsu']//h3[contains(text(), 'Arte')]")
        categoria_arte.click()
        capturar_pantalla("paso_3_seleccion_categoria_arte.png")  # Captura después de seleccionar la categoría de Arte
        time.sleep(3)  # Esperar a que se cargue la página de la categoría de Arte

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        capturar_pantalla("paso_4_final.png")  # Captura final después de hacer scroll hasta el final de la página


        # Mostrar mensaje de éxito
        print("Se ha explorado la sección 'Explorar lo mejor de Pinterest' y se ha seleccionado la categoría de Arte correctamente.")

    except Exception as e:
        # Mostrar mensaje de error si no se pudo completar la acción
        print(f"Error al explorar y seleccionar la categoría de Arte: {str(e)}")

    finally:
        # Cerrar el navegador 
        driver.quit()

# función para ejecutar la prueba
explorar_pinterest()

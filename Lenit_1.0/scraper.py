# scraper.py
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import user_agent_chrome, url

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent_chrome}")
    options.add_argument("--headless")
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def obtener_info():
    driver = get_driver()
    info = ""
    try:
        driver.get(url)
        contenedor = driver.find_element(By.ID, "the-python-tutorial")
        elementos = contenedor.find_elements(By.TAG_NAME, "p")
        parrafos = [elemento.text for elemento in elementos]
        info = "\n".join(parrafos)
    except NoSuchElementException:
        print("Elemento no encontrado")
    finally:
        driver.quit()
    return info

def obtener_ruta():
    driver = get_driver()
    diccionario = [] 
    try:
        driver.get(url)
        contenedor = driver.find_element(By.ID, "the-python-tutorial")
        elementos = contenedor.find_elements(By.CLASS_NAME, "toctree-l1")
        for elemento in elementos:
            try:
                link_element = elemento.find_element(By.TAG_NAME, "a")
                diccionario.append({
                    "Tema": link_element.text,
                    "Enlace": link_element.get_attribute("href")
                })
            except NoSuchElementException:
                print("No se encontró el enlace")
    except NoSuchElementException:
        print("Selector inválido")
    finally:
        driver.quit()
    ruta_texto = "\n".join([f"Tema: {e['Tema']}\nEnlace: {e['Enlace']}" for e in diccionario])
    return ruta_texto






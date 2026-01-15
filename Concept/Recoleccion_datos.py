import os

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--headless")
service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://docs.python.org/es/3/tutorial/index.html")

try:
    contenedor = driver.find_element(By.XPATH, '//*[@id="the-python-tutorial"]/div')
    direcciones = contenedor.find_elements(By.CLASS_NAME, "toctree-l1")
except NoSuchElementException:
    print("Invalid selector")

elementos = []
for elemento in direcciones:
    try:
        link_element = elemento.find_element(By.TAG_NAME, "a")
        elementos.append(
            {"Tema":link_element.text, "Enlace":link_element.get_attribute("href")}
        )
    except NoSuchElementException:
        print("No such element found")





driver.quit()
df = pd.DataFrame(elementos)

os.system("cls")
print("Data extrated correctly\n")
df.to_csv("temas_python.csv", index=False)

input("Press Enter to exit...")
print("Exiting...")


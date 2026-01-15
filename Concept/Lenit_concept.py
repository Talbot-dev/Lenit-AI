import os
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Web scraping
ua = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
url = "https://docs.python.org/3/tutorial/"
url2 = "https://roadmap.sh/python"

option = webdriver.ChromeOptions()
option.add_argument("--headless")
service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=option)

driver.get(url2)

req = requests.get(url, headers=ua)
soup2 = BeautifulSoup(req.text, "html.parser")

# Data extraction
tema_basico1 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Basic Syntax"]').text
tema_basico2 = driver.find_element(
    By.CSS_SELECTOR, 'g[data-title="Variables and Data Types"]'
).text
tema_basico3 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Conditionals"]').text
tema_basico4 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Loops"]').text
tema_basico5 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Dictionaries"]').text
tema_intermedio1 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Regular Expressions"]').text
tema_intermedio2 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Iterators"]').text
tema_intermedio3 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Object Oriented Programming"]').text
tema_intermedio4 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Arrays and Linked Lists"]').text
tema_intermedio5 = driver.find_element(By.CSS_SELECTOR, 'g[data-title="Decorators"]').text

driver.quit()

tema_python = soup2.find("section", id="the-python-tutorial").find("p").get_text()

# Execution of the program
while True:
    os.system("cls")
    print(
        """> Welcome to the first version of Lenit<
        
      Here's the information that you can access:
        
        1. What is python? 
        2. Learn Python (basic level)
        3. learn Python (intermediate level)  
            
    Want to finish the program? [type 'exit']     
        """
    )
    opcion = input(
        "Which topic would you like to learn today? [type the number of the option] "
    )

    if opcion == "1":
        os.system("cls")
        print("What is Python?", end="\n")
        print(f"\n{tema_python}", end="\n")
        input("\nPress enter to return...")

    elif opcion == "2":
        os.system("cls")
        print(
            f"""The basic topics that you can learn are: 
            
        1. {tema_basico1}
        2. {tema_basico2}
        3. {tema_basico3}
        4. {tema_basico4}
        5. {tema_basico5}"""
        )
        input("\nPress enter to return...")

    elif opcion == "3":
        os.system("cls")
        print(
            f"""The intermediate topics that you can learn are: 
            
        1. {tema_intermedio1}
        2. {tema_intermedio2}
        3. {tema_intermedio3}
        4. {tema_intermedio4}
        5. {tema_intermedio5}"""
        )
        input("\nPress enter to return...")

    elif opcion == "exit":
        os.system("cls")
        print("\nThank you for using Lenit\nExiting the program...")
        break

    else:
        os.system("cls")
        print("\nInvalid option, returning...\n")
        time.sleep(2)

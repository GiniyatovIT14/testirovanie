import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@test.com")

    # пустой .txt рядом со скриптом
    path = os.path.abspath("test.txt")
    open(path, "w").close()

    browser.find_element(By.ID, "file").send_keys(path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    if browser:
        browser.quit()
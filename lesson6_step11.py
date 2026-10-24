from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# поменять на registration2.html чтобы проверить падение с NoSuchElementException
link = "http://suninjuly.github.io/registration1.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # First name* — только в first_block, иначе зацепит Phone
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("Ivan")
    # Last name* — есть в reg1, нет в reg2 -> здесь падает с NoSuchElementException
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("Petrov")
    # Email*
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("ivan@test.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" in welcome

finally:
    time.sleep(10)
    if browser:
        browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"  # тот же код работает и для selects2.html
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    total = str(num1 + num2)

    Select(browser.find_element(By.ID, "dropdown")).select_by_value(total)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    if browser:
        browser.quit()
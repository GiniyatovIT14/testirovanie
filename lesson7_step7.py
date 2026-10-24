import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    if browser:
        browser.quit()
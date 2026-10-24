import time
from selenium.webdriver.common.by import By

def test_page_has_add_to_cart_button(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    print(f"\nТекст на кнопке: '{button.text}'")
    

    assert button is not None, "Кнопка добавления в корзину не найдена на странице!"
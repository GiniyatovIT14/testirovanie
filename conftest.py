import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: es, fr, ru, etc.')

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print(f"\n[Запуск браузера Chrome с языком: {user_language}]")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\n[Закрытие браузера]")
    browser.quit()
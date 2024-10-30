from email.policy import default
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ru, en, fr, deu, es')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nStart Chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        print("\nStart Firefox browser for test..")
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    if browser is not None:
        print("\nQuit browser..")
        browser.quit()

@pytest.fixture(scope="session")
def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config

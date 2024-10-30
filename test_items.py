from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from conftest import browser

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser):
    browser.get(link)

    time.sleep(30)

    button_add_to_cart = (wait(browser, 10).until
                          (EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))))
    assert button_add_to_cart.is_enabled(), 'Кнопка не кликабельна'

    button_add_to_cart.click()

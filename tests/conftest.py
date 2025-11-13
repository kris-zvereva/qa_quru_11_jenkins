import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function',autouse=True)
def set_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    # Настройки для Jenkins
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    browser.config.driver_options = options

    yield
    browser.quit()
import pytest
from selene import browser


@pytest.fixture(scope='function',autouse=True)
def set_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    # для Jenkins
    options = browser.config.driver_options
    options.add_argument('--headless=new')  # новый headless режим
    options.add_argument('--no-sandbox')  # нужно для Jenkins
    options.add_argument('--disable-dev-shm-usage')  # избегает проблем с памятью
    options.add_argument('--disable-gpu')  # отключает GPU

    yield
    browser.quit()
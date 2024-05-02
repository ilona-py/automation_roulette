import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from game_pages import Roulette


@pytest.fixture(scope='session')
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def roulette(get_driver):
    return Roulette(get_driver)


@pytest.fixture(scope="function")
def open_roulette(roulette):
    roulette.check_url(url=roulette.url)
    yield




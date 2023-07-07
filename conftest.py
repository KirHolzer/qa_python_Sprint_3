import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--window-size=1200,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

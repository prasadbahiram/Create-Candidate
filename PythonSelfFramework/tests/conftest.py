from selenium import webdriver
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()



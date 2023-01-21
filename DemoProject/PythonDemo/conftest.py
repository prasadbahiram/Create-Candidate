import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup():
    service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/angularpractice/")

    yield
    driver.close()

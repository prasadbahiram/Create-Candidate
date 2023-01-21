from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("")
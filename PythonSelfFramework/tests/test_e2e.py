from selenium import webdriver
import time
import pytest
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.implicitly_wait(5)

        #    //a[contains(@href,'shop')]            a[href*='shop']
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        print(len(products))
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert").text
        assert "Success! Thank you!" in successText









from django.test import TestCase
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestTest1:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1382, 744)
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("armani")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-success").click()

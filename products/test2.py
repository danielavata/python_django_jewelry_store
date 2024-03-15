from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test2(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1382, 744)
        self.driver.find_element(By.LINK_TEXT, "Produse").click()
        self.driver.find_element(By.LINK_TEXT, "Ceasuri").click()
        self.driver.find_element(By.LINK_TEXT, "Bijuterii").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-xl-4:nth-child(6) .card-body > .btn").click()
        self.driver.find_element(By.NAME, "quantity").send_keys("2")
        self.driver.find_element(By.NAME, "quantity").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn > img").click()


# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest3():

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()
  def test_test3(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("danielavata")
    self.driver.find_element(By.ID, "id_password").send_keys("Clientmagazin2024")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.ID, "id_email").click()
    self.driver.find_element(By.ID, "id_email").send_keys("danielavata@gmail.com")
    self.driver.find_element(By.ID, "id_phone_number").click()
    self.driver.find_element(By.ID, "id_phone_number").send_keys("0726237141")
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("Intrebare")
    self.driver.find_element(By.ID, "id_content").click()
    self.driver.find_element(By.ID, "id_content").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
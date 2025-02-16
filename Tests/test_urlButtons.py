# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestUrlButtons():
  #for each of these tests, it's check if the button is move to the correct place by checking the url adress
  
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    self.driver=webdriver.Edge()
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(1920, 996)
    self.driver.find_element(By.ID, "username").send_keys("Heath93")
    self.driver.find_element(By.ID, "password").send_keys("s3cret")
    self.driver.find_element(By.CSS_SELECTOR, "[data-test=\"signin-submit\"]").click()
    time.sleep(3)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bankAccountButton(self):
    
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiTypography-root").click()
     
    # Wait for the navigation to complete
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/bankaccounts")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/bankaccounts", f"Expected URL to be 'http://localhost:3000/bankaccounts', but got '{current_url}'"
  
  def test_logOutButton(self):
    
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"sidenav-signout\"]").click()
    # Wait for the navigation to complete
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/signin")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/signin", f"Expected URL to be 'http://localhost:3000/signin', but got '{current_url}'"
    
  

  def test_myAccountBotton(self):
    
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .MuiTypography-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .MuiTypography-root").click()
    time.sleep(3)
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/user/settings")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/user/settings", f"Expected URL to be 'http://localhost:3000/user/settings', but got '{current_url}'"
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
  
  def test_newTransctionButton(self):
    
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"nav-top-new-transaction\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"nav-top-new-transaction\"]")
    time.sleep(3)
    # Wait for the navigation to complete
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/transaction/new")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/transaction/new", f"Expected URL to be 'http://localhost:3000/transaction/new', but got '{current_url}'"
    
    # actions = ActionChains(self.driver)
    # actions.double_click(element).perform()
  
  def test_notifictionButton(self):
    
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4) .MuiTypography-root").click()
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/notifications")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/notifications", f"Expected URL to be 'http://localhost:3000/notifications', but got '{current_url}'"
  
  def test_homeButton(self):
    
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(3) .MuiButtonBase-root:nth-child(1) .MuiTypography-root").click()
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost:3000/")
    )

    # Verify the current URL
    current_url = self.driver.current_url
    assert current_url == "http://localhost:3000/", f"Expected URL to be 'http://localhost:3000/', but got '{current_url}'"
  

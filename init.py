from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Ensure ChromeDriver is in /usr/bin/ and executable
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'))

driver.get("https://www.google.com/")
driver.implicitly_wait(3)
search_element = driver.find_element(By.ID, "APjFqb")
search_element.send_keys("Ahmed Al Balochi")
search_btn = driver.find_element(By.NAME, 'btnK').click()
  
time.sleep(5)
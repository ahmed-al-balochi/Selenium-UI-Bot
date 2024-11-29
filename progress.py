from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Ensure ChromeDriver is in /usr/bin/ and executable
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'))

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(120)
download = driver.find_element(By.ID, 'downloadButton').click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
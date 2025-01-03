# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:43:04 2025

@author: Bharat Shirsath
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# search website
driver.get(r"https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

# Wait for the page to load
driver.implicitly_wait(60)
driver.maximize_window()
driver.refresh()

# searching "New York" city in search box
city_filter = WebDriverWait(driver, 10).until(EC.presence_of_elements_located((By.XPATH, "//*[@id='example_filter']/label/input"))).send_keys("New York")
time.sleep(3)

# Close the browser
driver.quit()

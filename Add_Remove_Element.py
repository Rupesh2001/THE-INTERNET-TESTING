from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Install and initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "http://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()

# Click on Add/Remove Elements
ADD_REMOVE = driver.find_element(By.XPATH, "//a[normalize-space()='Add/Remove Elements']")
ADD_REMOVE.click()
time.sleep(2)

# Click on Add Element button
ADD_ELEMENT = driver.find_element(By.XPATH, "//button[normalize-space()='Add Element']")
ADD_ELEMENT.click()
time.sleep(2)

# Locate the added button
button = driver.find_element(By.XPATH, "//div[@id='elements']/button")

# Check if the button is displayed
if button.is_displayed():  # Corrected syntax
    print("Button is displayed")
    driver.execute_script("arguments[0].remove();", button)  # Remove the button using JS
   # driver.execute_script("arguments[0].style.display = 'none';", button) to hide button
else:
    print("Button is not displayed")

time.sleep(5)
driver.quit()

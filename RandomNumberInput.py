from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random


# Install and initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "http://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)

# Click on the link
input_link = driver.find_element(By.LINK_TEXT, "Inputs")
input_link.click()
time.sleep(3)

# Enter a random number between 1 and 100 in the input field
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
random_number = "977" + str(random.randint(10000, 99999))
input_field.send_keys(random_number)
time.sleep(3)

# Close the browser
driver.quit()



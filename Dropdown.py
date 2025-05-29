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
time.sleep(5)
dropdown_link = driver.find_element(By.LINK_TEXT, "Dropdown")
dropdown_link.click()
time.sleep(5)
dropdown = driver.find_element(By.ID, "dropdown")
dropdown.click()
time.sleep(5)
option1 = driver.find_element(By.XPATH, "//option[@value='1']")
option1.click()
print(option1.text)
time.sleep(5)
option2 = driver.find_element(By.XPATH, "//option[@value='2']")
option2.click()
print(option2.text)
time.sleep(5)
driver.quit()

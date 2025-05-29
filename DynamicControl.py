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
DynamicControl = driver.find_element(By.XPATH,"//a[normalize-space()='Dynamic Controls']")
DynamicControl.click()
time.sleep(5)
RemoveButton = driver.find_element(By.XPATH,"//button[normalize-space()='Remove']")
RemoveButton.click()
time.sleep(5)
AddButton = driver.find_element(By.XPATH,"//button[normalize-space()='Add']")
AddButton.click()
time.sleep(5)
EnableButton = driver.find_element(By.XPATH,"//button[normalize-space()='Enable']")
EnableButton.click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
time.sleep(5)
DisableButton = driver.find_element(By.XPATH,"//button[normalize-space()='Disable']")
DisableButton.click()
time.sleep(5)
driver.quit()




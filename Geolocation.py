from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#install driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Url
url = "http://the-internet.herokuapp.com/"

driver.get(url)
driver.maximize_window()
time.sleep(2)
geolocation = driver.find_element(By.XPATH,"//a[normalize-space()='Geolocation']")
geolocation.click()
time.sleep(2)
button = driver.find_element(By.XPATH,"//button[normalize-space()='Where am I?']")
button.click()
time.sleep(2)
lat = driver.find_element(By.XPATH,"//div[@id='lat-value']")
print(lat.text)
long = driver.find_element(By.XPATH,"//div[@id='long-value']")
print(long.text)
time.sleep(5)
driver.quit()
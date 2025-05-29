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
EntryAd = driver.find_element(By.XPATH, "//a[text()='Entry Ad']")
EntryAd.click()
time.sleep(5)
closeModel = driver.find_element(By.XPATH,"//p[normalize-space()='Close']")
closeModel.click()
time.sleep(5)

driver.quit()
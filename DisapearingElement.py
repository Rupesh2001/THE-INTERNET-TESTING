from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Install and initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "http://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
disappearing_element_link = driver.find_element(By.LINK_TEXT, "Disappearing Elements")
disappearing_element_link.click()
time.sleep(5)
for _ in range(5):
    driver.refresh()
    time.sleep(5)
    try:
       #  gallery = WebDriverWait(driver, 10).until(
       # EC.visibility_of_element_located((By.LINK_TEXT, "Gallery"))
       if(driver.find_element(By.LINK_TEXT, "Gallery").is_displayed()):
         print("Gallery is displayed")   
    except:
        print("Gallery is not displayed")
time.sleep(5)
driver.quit()
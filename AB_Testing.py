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
abTesting = driver.find_element(By.XPATH,"//a[normalize-space()='A/B Testing']")
abTesting.click()
time.sleep(2)
link_url = "http://the-internet.herokuapp.com/abtest"
if(driver.current_url == link_url):
    {
        print("A/B Testing Successfull")
    }
time.sleep(2)
previous_url = "http://the-internet.herokuapp.com/"
driver.get(previous_url)
time.sleep(2)
driver.quit()
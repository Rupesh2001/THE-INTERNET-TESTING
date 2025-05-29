from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(service=(ChromeService(ChromeDriverManager().install())))

url = "http://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
Auth = driver.find_element(By.XPATH,"//a[normalize-space()='Basic Auth']")
Auth.click()
time.sleep(2)
try:
    username = "admin"
    password = "admin"
    auth_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    driver.get(auth_url)
    Basic = driver.find_element(By.XPATH,"//h3[normalize-space()='Basic Auth']")
    if(Basic.text=="Basic Auth"):
        {
            print("sign-in successful")
        }
except:   
    print("wrong")
        
   


time.sleep(5)
driver.quit()
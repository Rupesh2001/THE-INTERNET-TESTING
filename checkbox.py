from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
chklink = driver.find_element(By.XPATH,"//a[normalize-space()='Checkboxes']")
chklink.click()
time.sleep(2)
input1 = driver.find_element(By.XPATH,"//input[1]")
input2 = driver.find_element(By.XPATH,"//input[2]")
if(input1.is_selected()):
    print("Checkbox 1 is selected")
else:
    print("Checkbox 1 is not selected")
    input1.click()
    time.sleep(5)
if(input2.is_selected()):
    print("Checkbox 2 is selected")
else:
    print("Checkbox 2 is not selected")
    input2.click()
    time.sleep(5)
time.sleep(5)
driver.quit()
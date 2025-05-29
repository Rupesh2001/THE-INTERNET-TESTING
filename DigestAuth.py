from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Digest Authentication']").click()
time.sleep(5)
pyautogui.typewrite("admin")
pyautogui.press("tab")
pyautogui.typewrite("admin")
pyautogui.press("enter")
time.sleep(3)
if(driver.find_element(By.XPATH,"//h3[normalize-space()='Digest Auth']").text=="Digest Auth"):
    print("sign-in successful")
else:
    print("you press cancel")

time.sleep(5)
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/basic_auth")

# Give the browser a moment to open the Basic Auth prompt
time.sleep(2)

# Now use PyAutoGUI to type the username, press Tab, type the password, and press Enter
pyautogui.typewrite("admin")
pyautogui.press("tab")
pyautogui.typewrite("admin")

# Press Enter to click "Sign in"
#pyautogui.press("enter")

# OR press Escape if you want to simulate Cancel (depending on the OS/browser)
pyautogui.press("esc")
Basic = driver.find_element(By.XPATH,"//h3[normalize-space()='Basic Auth']")
if(Basic.text=="Basic Auth"):
        {
            print("sign-in successful")
        }
else:
        {
            print("you press cancel")     
        }
       
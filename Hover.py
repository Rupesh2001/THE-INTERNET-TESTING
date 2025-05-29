from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Install and initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "http://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(5)

Hover_link = driver.find_element(By.XPATH, "//a[contains(text(),'Hovers')]")
Hover_link.click()
time.sleep(5)
Hover_element = driver.find_element(By.XPATH,"//div[@class='example']//div[1]//img[1]")
actions = ActionChains(driver)
actions.move_to_element(Hover_element).perform()
time.sleep(5)
try:
    Hover_text = driver.find_element(By.XPATH,"//h5[normalize-space()='name: user1']")
    print("Hover text is displayed: ", Hover_text.text)
    time.sleep(5)
    Hover_link = driver.find_element(By.XPATH, "//div[@class='example']//div[1]//div[1]//a[1]")
    Hover_link.click()
    time.sleep(5)
    NotFoundCase = driver.find_element(By.XPATH,"//h1[normalize-space()='Not Found']")
    if(NotFoundCase.text == "Not Found"):
        print("User1 page is not Found")
        time.sleep(5)
    else:
        print("User1 page is Found")
    time.sleep(5)
except:
    print("Hover text is not displayed")
time.sleep(5)



driver.quit()
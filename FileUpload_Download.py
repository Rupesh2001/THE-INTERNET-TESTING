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

fileUpload_link = driver.find_element(By.XPATH,"//a[normalize-space()='File Upload']")
fileUpload_link.click()
time.sleep(5)
fileupload = driver.find_element(By.XPATH,"//input[@id='file-upload']")
fileupload.send_keys(r"e:\photos\ABC\abc\IMG_20241105_163609.jpg")
time.sleep(5)
uploadButton = driver.find_element(By.XPATH,"//input[@id='file-submit']")
uploadButton.click()
time.sleep(5)
try:
    driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
    print("File Uploaded Successfully")
except:
    print("File Upload Failed")
time.sleep(5)
driver.get(url)
time.sleep(5)
fileDownload_link = driver.find_element(By.XPATH,"//a[normalize-space()='File Download']")
fileDownload_link.click()
time.sleep(5)
fileDownload = driver.find_element(By.XPATH,"//a[normalize-space()='random_data.txt']")
fileDownload.click()

time.sleep(5)





driver.quit()
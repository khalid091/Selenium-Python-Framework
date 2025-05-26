from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="F:\Automation\SeleniumPython\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "central-featured"))
)

input_element = driver.find_element(By.ID, "searchInput")
input_element.clear()
input_element.send_keys("Khalid Bahaj" + Keys.ENTER)



WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "2022–23 IR Tanger season"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "2022–23 IR Tanger season")
link.click()

time.sleep(10)

driver.quit()
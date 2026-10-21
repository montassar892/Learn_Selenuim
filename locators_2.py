from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.ID, "userEmail").send_keys("montassarlabidi892@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("123456")
driver.find_element(By.ID, "login").click()

time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    driver = webdriver.Firefox()
    time.sleep(8)
    driver.get("https://the-internet.herokuapp.com/login")
    input_user = driver.find_element(By.NAME, "username")
    input_user.send_keys("tomsmith")
    input_password = driver.find_element(By.NAME, "password")
    input_password.send_keys("SuperSecretPassword!")
    time.sleep(8)
    log_button = driver.find_element(By.CLASS_NAME, "radius")
    log_button.click()
    time.sleep(8)
except Exception as e:
    print(" An Error occured")

finally:
    time.sleep(8)
    driver.quit() 

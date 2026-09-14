from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Edge()
time.sleep(8)
try:
    driver.get("https://www.google.com/")
    search_bar = driver.find_element(By.NAME,"q")
    time.sleep(8)
    search_bar.send_keys("selenium basics" + Keys.ENTER)
    #search_bar.send_keys("selenium basics" + Keys.ENTER)
    time.sleep(15)
except AssertionError as e:
    print(f"Test Failed - {e}")
except Exception as e:
    print(f"Error occured: {e}")
finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try :
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(2)
    print("Triggering Simple Alert")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    time.sleep(2)
    alert1 = driver.switch_to.alert
    alert1.dismiss()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert2 = driver.switch_to.alert
    alert.send_keys("Hello")
    alert2.accept()
    result_text = driver.find_element(By.ID,"result").text
    assert "You entered: Hello" in result_text
    print("Assert passed!!!!!!!!")
except Exception as e:
    print("Error thrown")
finally:
    time.sleep(2)
    driver.quit()




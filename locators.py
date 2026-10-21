from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time 

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.implicitly_wait(5)
#email
driver.find_element(By.NAME,"email").send_keys("montassarlabidi892@gmail.com")
driver.find_element(By.NAME,"name").send_keys("montassarlabidi")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()



#dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")

driver.find_element(By.XPATH, "//label[@for='inlineRadio2']").click()
driver.find_element(By.NAME, "bday").send_keys("12/18/1997")

driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(10)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print (countries)

for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
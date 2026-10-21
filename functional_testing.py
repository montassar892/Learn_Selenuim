from selenium import webdriver
from selenium.webdriver.common.by import By

actualList = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys('ber')
results = driver.find_element(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,'h4').text)
    

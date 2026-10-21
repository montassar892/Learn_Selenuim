from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()   # choose the driver that will be using instantiate the class 
driver.get("https://www.selenium.dev/")
driver.implicitly_wait(8)     #8second  timeout for all the element to be found 

my_element = driver.find_element(By.CLASS_NAME,'fab fa-linkedin-in')
print(f"{my_element.text}")

my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
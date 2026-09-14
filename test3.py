from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 


driver = webdriver.Firefox()
try:
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_element = driver.find_element(By.ID,"dropdown")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option 1")
    time.sleep(2)
    current_selection = dropdown.first_selected_option.text
except Exception as e:
    print("An Error has occured")
finally:
    time.sleep(10)
    driver.quit()

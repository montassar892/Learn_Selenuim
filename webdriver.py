from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. SETUP: This part tells Python to open the Chrome browser automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. NAVIGATION: Tell the browser to go to our practice website
    print("Opening the website...")
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Give the page 2 seconds to load so we don't rush it
    time.sleep(2)

    # 3. INTERACTION: Finding elements and typing
    # We use cssSelector because these elements have unique IDs
    print("Entering credentials...")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # 4. ACTION: Clicking the button
    # We use cssSelector for the button as well
    print("Clicking login button...")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait a moment to see the result
    time.sleep(3)

    # 5. VERIFICATION: Did it work? 
    # We look for the "Success" message on the new page
    success_message = driver.find_element(By.ID, "flash").text
    
    if "You logged into a secure area!" in success_message:
        print("SUCCESS: Login worked perfectly!")
    else:
        print("FAILURE: Login failed.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. CLEANUP: Close the browser window
    print("Closing browser in 3 seconds...")
    time.sleep(3)
    driver.quit()

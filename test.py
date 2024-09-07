import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()

# open the webpage
driver.get("http://www.instagram.com")

try:
    # wait for username and password fields to be clickable
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
    )

    # enter username and password
    username.clear()
    username.send_keys("original_trilogy_dpk24")
    password.clear()
    password.send_keys("palashdevkanishk")

    # target the login button and click it
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    button.click()

    # Wait for some time to see if an alert appears (optional)
    time.sleep(5)

    # Try to handle an alert if it appears
    try:
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert.dismiss()
        print("Alert dismissed")
    except:
        print("No alert present")

finally:
    # Cleanup and close the browser
    driver.quit()

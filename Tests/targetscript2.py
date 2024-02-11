from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

# Initialize Chrome WebDriver with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# Step 1: Open the Target website
driver.get("https://www.target.com")

# Step 2: Click SignIn button
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/nav/a[4]/span")
sign_in_button.click()
sleep(4)

# Step 3: Click SignIn from side navigation
side_sign_in_button = driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div[2]/ul/li[1]/a/span")
side_sign_in_button.click()
sleep(4)

# Step 4: Verify SignIn page opened
sign_in_page_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/h1").text

if sign_in_page_text == "Sign into your Target account":
    print("PASS: SignIn page opened successfully.")

    # Close the browser window
    driver.quit()
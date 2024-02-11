from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Initialize Chrome WebDriver with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# Step 1: Open the Target website
driver.get("https://www.target.com/")

# Step 2: Click SignIn button
sign_in_button_xpath = "/html/body/div[1]/div[2]/div[2]/div/nav/a[4]/span"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath))).click()

# Step 3: Click SignIn from side navigation
side_sign_in_button_xpath = "/html/body/div[10]/div/div/div[2]/ul/li[1]/a"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, side_sign_in_button_xpath))).click()

# Step 4: Verify SignIn page opened
sign_in_page_text_xpath = "/html/body/div[1]/div/div/div/div[1]/div/h1/span"
sign_in_button_xpath = "/html/body/div[1]/div/div/div/div[1]/div/form/button"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, sign_in_page_text_xpath)))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, sign_in_button_xpath)))

sign_in_page_text = driver.find_element(By.XPATH, sign_in_page_text_xpath).text
sign_in_button_present = driver.find_element(By.XPATH, sign_in_button_xpath).is_displayed()

if sign_in_page_text == "Sign into your Target account" and sign_in_button_present:
    print("PASS: SignIn page opened successfully.")
else:
    print("FAIL: SignIn page did not open.")

# Close the browser window
driver.quit()


'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# Initialize Chrome WebDriver with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# Test Case: Users can navigate to SignIn page
try:
    # Step 1: Open the Target website
    driver.get("https://www.target.com")

    # Step 2: Click SignIn button
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/nav/a[4]/span")
    sign_in_button.click()

    # Step 3: Click SignIn from side navigation
    side_sign_in_button = driver.find_element(By.XPATH, "//html/body/div[1]/div[2]/div[2]/div/nav/a[4]/span")
    side_sign_in_button.click()


    # Step 4: Verify SignIn page opened
    sign_in_page_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/h1/span)]").text
    if sign_in_page_text == "Sign into your Target account":
        print("PASS: SignIn page opened successfully.")
    else:
        print("FAIL: SignIn page did not open.")

except Exception as e:
    print("Exception occurred:", e)

finally:
    # Close the browser window
    driver.quit()

'''
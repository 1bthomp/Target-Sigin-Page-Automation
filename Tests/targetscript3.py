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

# This opens up the target website in the browser
driver.get("https://target.com")

# User will click on sign in button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(4)

# User clicks on Side Nav Sign in button
# (driver.find_element(By.XPATH, "//a[@href='/account']").click())
(driver.find_element(By.XPATH, "//a[@class='styles__StyledLink-sc-vpsldm-0 styles__ListLink-sc-diphzn-2 fkwerm gcgPXN']").click())
sleep(4)

# for my own reference
# <a href="/account" data-test="accountNav-signIn" class="styles__StyledLink-sc-vpsldm-0 styles__ListLink-sc-diphzn-2 fkwerm gcgPXN"><span class="styles__ListItemText-sc-diphzn-1 jaMNVl">Sign in</span></a>

# User Should be on the sign-in page. Below script will verify if user is on the right place
sign_in_page_check = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text

# for my own reference
# <h1 class="styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa"><span>Sign into your Target account</span></h1>

# Script will show if user is really on sign in page. this message will print in the terminal
if sign_in_page_check == "Sign into your Target account":
    print("PASS: SignIn page opened successfully.")

# Exits the browser
driver.quit()




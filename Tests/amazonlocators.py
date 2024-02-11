from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# IDs:
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'searchDropdownBox')

# Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

# Multiple attr
driver.find_element(By.XPATH, "//input[@tabindex='0' and @placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//select[@class='nav-search-dropdown "
                              "searchSelect nav-progressive-attrubute nav-progressive-search-dropdown']")
# Partial attr => contains()
driver.find_element(By.XPATH, "//select[contains(@class,'search-dropdown')]")
driver.find_element(By.XPATH, "//select[contains(@class,'search-dropdown') and @ame='url']")

# text()
driver.find_element(By.XPATH, "//span[text()='Winter Sale deals for your home']")
# text() + attr
driver.find_element(By.XPATH, "//span[text()='Winter Sale deals for your home' and "
                              "@class='a-truncate-full a-offscreen']")

# text() + contains()

#########################################################################################################################################################################

# HW #2

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email Field
driver.find_element(By.ID, "ap_email")

# Continue Button
driver.find_element(By.XPATH, "//input[@id='continue']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[@href'/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")

# Privacy Notice Link
driver.find_element(By.XPATH, "//a[@href'/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")

# Need help link
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?') and @class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.XPATH, "//a[@id['auth-fpp-link-bottom']")

# Other issues with Sign-in link was not available on this current version

# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id=['createAccountSubmit']")

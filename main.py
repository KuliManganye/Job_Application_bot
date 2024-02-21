from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os


# Environmental Variables
load_dotenv()


linked_in_password = os.getenv("LINKED_IN_PASSWORD")
email_address = os.getenv("EMAIL_ADDRESS")
URL = os.getenv("URL")

# keep the Chrome Browser Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open the specific page you want to redirect to:
driver.get(URL)

# sign in to your linked_In profile:
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

# Add your details: Email and Password
email_or_phone = driver.find_element(By.ID, value="username")
email_or_phone.send_keys(email_address)

password = driver.find_element(By.ID, value="password")
password.send_keys(linked_in_password)

# Click on the sign-in button:
sign_in_button = driver.find_element(By.CLASS_NAME, value="login__form_action_container")
sign_in_button.click()

# click on the apply button:
apply = driver.find_element(By.ID, value="ember187")
apply.click()

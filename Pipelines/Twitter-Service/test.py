import time
import sys
import os
from utils import TwitterService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from selenium import webdriver
from config import Config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



print(Config.USERNAME_TWITTER)
print(Config.PASSWORD_TWITTER)
print(Config.EMAIL_TWITTER)
driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")
username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username_input.send_keys(Config.USERNAME_TWITTER)
username_input.send_keys(Keys.ENTER)
time.sleep(2)

try:
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(Config.PASSWORD_TWITTER)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
except Exception as e:
    print(f"An error occurred: {e}")
    email_input = driver.find_element(By.TAG_NAME, "input")
    email_input.send_keys(Config.EMAIL_TWITTER)
    email_input.send_keys(Keys.RETURN)
    print("Email entered")
    time.sleep(5)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(Config.PASSWORD_TWITTER)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
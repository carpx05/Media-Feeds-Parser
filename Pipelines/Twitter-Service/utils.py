from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TwitterService:
    def __init__(self):
        # Initialize the Selenium WebDriver instance
        self.driver = webdriver.Chrome()

    def perform_login(self, username, password, email):
        """
        Attempts to log in to the application using the provided username and password.
        If the login fails and an email field is required, the email is entered before reattempting the password.

        Args:
            username (str): The username to be used for login.
            password (str): The password to be used for login.
            email (str): The email to be entered if required during login.

        Raises:
            Exception: If there is an issue locating or interacting with the input elements.
        """
        try:
            self.driver.get("https://x.com/i/flow/login")
            username_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
            username_input.send_keys(username)
            username_input.send_keys(Keys.ENTER)
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
            email_input = self.driver.find_element(By.TAG_NAME, "input")
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)
            print("Email entered")
            time.sleep(5)

            password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)

    def navigate_to_home(self):
        self.driver.get("https://x.com/home")


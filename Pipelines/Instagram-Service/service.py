import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from config import Config

TAG = "Instagram-Service/service.py"


class InstagramService:
    """
    A class to represent an Instagram service.
    """

    def __init__(self, post_data):
        self.driver = webdriver.Chrome()
        self.post_data = post_data.strip()
        self.wait = WebDriverWait(self.driver, 10)

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
            self.driver.get(Config.LOGIN_INSTAGRAM)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'input[name="username"]')
                )
            ).send_keys(Config.USERNAME_INSTAGRAM + Keys.ENTER)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'input[name="password"]')
                )
            ).send_keys(Config.PASSWORD_INSTAGRAM + Keys.ENTER)
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//div[text()="Not Now"]'))
            ).click()
            log(TAG, LogType.INFO, "Logged in successfully.")
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while logging in: {e}")

    def navigate_to_home(self):
        """
        Navigates to the home page of the application.
        """
        try:
            self.driver.get(Config.HOME_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Home.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the home page: {e}",
            )

    def save_cookies(self, username: str, password: str, path: str) -> None:
        """
        Saves the cookies to a file.
        """
        self.login(username, password)
        try:
            json_object = json.dumps(self.driver.get_cookies())

            with open(path, "w") as outfile:
                outfile.write(json_object)
            log(TAG, LogType.INFO, "Cookies saved successfully.")
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while saving cookies: {e}")

    def load_cookies(self, path: str) -> WebDriver:
        """
        Loads the cookies from a file.
        """
        self.driver.get(Config.LOGIN_INSTAGRAM)

        f = open(path)
        cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        time.sleep(1)

        self.driver.refresh()
        time.sleep(1)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
        ).click()
        time.sleep(1)

        return self.driver

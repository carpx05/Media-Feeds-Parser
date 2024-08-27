import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TwitterService:
    """
    A class to represent a Twitter service.
    """
    def __init__(self):
        # Initialize the Selenium WebDriver instance
        self.driver = webdriver.Chrome()
        self.tweet_data = tweet_data.strip()

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
        """
        Navigates to the home page of the application.
        """
        self.driver.get("https://x.com/home")

    def parse_tweet(self, tweet_data):
        """
        Parses the tweet data and extracts relevant information.
        """

        lines = self.tweet_data.strip().splitlines()

        username = lines[0].replace("Tweet Text: ", "").strip()
        userid = lines[1].strip()
        hours_ago = int(lines[3].replace("h", "").strip())

        tweet_text_lines = lines[4:-5]  
        tweet_text = ' '.join(line.strip() for line in tweet_text_lines)

        current_time = datetime.now()
        time_posted = current_time - timedelta(hours=hours_ago)
        time_posted_str = time_posted.strftime('%Y-%m-%d %H:%M:%S')

        replies = lines[-4].strip()
        retweets = lines[-3].strip()
        likes = lines[-2].strip()
        reach = lines[-1].strip()

        print(f"Username: {username}")
        print(f"User ID: {userid}")
        print(f"Time Posted (Approx.): {time_posted_str}")
        print(f"Tweet Text: {tweet_text}")
        print(f"Replies: {replies}")
        print(f"Retweets: {retweets}")
        print(f"Likes: {likes}")
        print(f"Reach: {reach}\n")

    def parse_timeline(self):
        """
        Parses the timeline of the user and extracts relevant tweet information.
        MEDIA ELEMENTS ARE NOT SUPPORTED IN THIS VERSION.
        """
        self.navigate_to_home()
        tweet_elements = self.driver.find_elements(By.XPATH, "//div[@data-testid='cellInnerDiv']")
        for tweet_element in tweet_elements:

            tweet_data = tweet_element.text
            self.parse_tweet(tweet_data)


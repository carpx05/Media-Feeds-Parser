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
    def __init__(self, tweet_data):
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

    def scroll_and_load_timeline(self, n=5):
        """
        Scrolls the timeline and loads more tweets.
        """
        for _ in range(n):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    def parse_timeline(self, total_scroll=5):
        """
        Parses the timeline of the user and extracts relevant tweet information.
        MEDIA ELEMENTS ARE NOT SUPPORTED IN THIS VERSION.
        """
        self.navigate_to_home()
        time.sleep(5)
        
        self.scroll_and_load_timeline(total_scroll)
        tweet_elements = self.driver.find_elements(By.XPATH, "//div[@data-testid='cellInnerDiv']")
        for tweet_element in tweet_elements:

            tweet_data = tweet_element.text
            extracted_text = self.parse_tweet(tweet_data)
            extracted_media = self.extract_tweet_media(tweet_element)

    def parse_tweet(self, tweet_data):
        """
        Parses the tweet data and extracts relevant information.
        Returns a dictionary containing the extracted data.
        """

        lines = self.tweet_data.strip().splitlines()

        username = lines[0].replace("Tweet Text: ", "").strip()
        userid = lines[1].strip()
        time_info = lines[3].strip()

        try:
            if 'h' in time_info:
                hours_ago = int(time_info.replace("h", "").strip())
                current_time = datetime.now()
                time_posted = current_time - timedelta(hours=hours_ago)

            else:
                time_posted = datetime.strptime(time_info + f" {datetime.now().year}", '%b %d %Y')
        except ValueError as e:
            print(f"Error parsing time information: {e}")
            return None
        
        time_posted_str = time_posted.strftime('%Y-%m-%d %H:%M:%S')
        tweet_text_lines = lines[4:-5]  
        tweet_text = ' '.join(line.strip() for line in tweet_text_lines)

        replies = lines[-4].strip()
        retweets = lines[-3].strip()
        likes = lines[-2].strip()
        reach = lines[-1].strip()
        return {
            "username": username,
            "userid": userid,
            "time_posted": time_posted_str,
            "tweet_text": tweet_text,
            "replies": replies,
            "retweets": retweets,
            "likes": likes,
            "reach": reach
        }

    def extract_tweet_media(self, tweet_element):
        """
        Extracts media elements from a tweet element.
        """
        media_data = {
            "profile_image": None,
            "media": []
        }
        try:
            media_elements = tweet_element.find_elements(By.CSS_SELECTOR, "img, video")
            for idx, media in enumerate(media_elements):
                media_src = media.get_attribute('src')
                if idx == 0:
                    media_data["profile_image"] = media_src
                elif media_src:
                    media_data["media"].append(media_src)
                else:
                    media_data["media"].append("Not found")
        except Exception as _:
            media_data["media"].append("Not found")
        return media_data

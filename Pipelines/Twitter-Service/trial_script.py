import time
import sys
import os
from utils import TwitterService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from selenium import webdriver
from config import Config


# driver = webdriver.Chrome()

# time.sleep(2)
twitter_service = TwitterService()
twitter_service.perform_login(
    Config.USERNAME_TWITTER, Config.PASSWORD_TWITTER, Config.EMAIL_TWITTER
)
twitter_service.navigate_to_home()
time.sleep(2)

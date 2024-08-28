import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Twitter Credentials
    USERNAME_TWITTER = os.getenv("USERNAME_TWITTER")
    PASSWORD_TWITTER = os.getenv("PASSWORD_TWITTER")
    EMAIL_TWITTER = os.getenv("EMAIL_TWITTER")

    # Twitter Navigation
    HOME_TWITTER = os.getenv("HOME_TWITTER")
    LOGIN_TWITTER = os.getenv("LOGIN_TWITTER")

    # Instagram Credentials
    USERNAME_INSTAGRAM = os.getenv("USERNAME_INSTAGRAM")
    PASSWORD_INSTAGRAM = os.getenv("PASSWORD_INSTAGRAM")

    # Instagram Navigation
    HOME_INSTAGRAM = os.getenv("HOME_INSTAGRAM")
    LOGIN_INSTAGRAM = os.getenv("LOGIN_INSTAGRAM")

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    USERNAME_TWITTER = os.getenv("USERNAME_TWITTER")
    PASSWORD_TWITTER = os.getenv("PASSWORD_TWITTER")
    EMAIL_TWITTER = os.getenv("EMAIL_TWITTER")

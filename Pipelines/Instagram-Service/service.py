import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from config import Config
from utils.logger import LogType, log

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
            self.driver.get(username)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'input[name="username"]')
                )
            ).send_keys(password + Keys.ENTER)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'input[name="password"]')
                )
            ).send_keys(password + Keys.ENTER)
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[@role='button' and contains(@class, 'x1i10hfl')]",
                        )
                    )
                )
                element.click()
            except Exception as _:
                log(TAG, LogType.WARNING, f"remember login info not required.")
            try:
                button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//button[contains(@class, '_a9--') and text()='Not Now']",
                        )
                    )
                )
                button.click()
            except Exception as _:
                log(TAG, LogType.WARNING, f"Notification not required.")
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

    def navigate_to_explore(self):
        """
        Navigates to the explore page of the application.
        """
        try:
            self.driver.get(Config.EXPLORE_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Explore.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the explore page: {e}",
            )

    def navigate_to_login_activity(self):
        """
        Navigates to the login activity page of the application.
        """
        try:
            self.driver.get(Config.LOGIN_ACTIVITY_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Login Activity.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the login activity page: {e}",
            )

    def navigate_to_profile(self, username):
        """
        Navigates to the profile page of the application.
        """
        try:
            self.driver.get(f"{Config.HOME_INSTAGRAM}/{username}/")
            log(TAG, LogType.INFO, "Navigated, Instagram Profile.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the profile page: {e}",
            )

    def navigate_to_interactions_story_replies(self):
        """
        Navigates to the interactions story replies page of the application.
        """
        try:
            self.driver.get(Config.INTERACTIONS_STORY_REPLIES_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Interactions Story Replies.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the interactions story replies page: {e}",
            )

    def navigate_to_interactions_reviews(self):
        """
        Navigates to the interactions reviews page of the application.
        """
        try:
            self.driver.get(Config.INTERACTIONS_REVIEWS_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Interactions Reviews.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the interactions reviews page: {e}",
            )
        
    def navigate_to_followers(self, username):
        """
        Navigates to the followers page of the application.
        """
        try:
            self.driver.get(f"{Config.HOME_INSTAGRAM}/{username}/followers/")
            log(TAG, LogType.INFO, "Navigated, Instagram Followers.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the followers page: {e}",
            )

    def navigate_to_following(self, username):
        """
        Navigates to the following page of the application.
        """
        try:
            self.driver.get(f"{Config.HOME_INSTAGRAM}/{username}/following/")
            log(TAG, LogType.INFO, "Navigated, Instagram Following.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the following page: {e}",
            )
    
    def navigate_to_interactions_comments(self):
        """
        Navigates to the interactions comments page of the application.
        """
        try:
            self.driver.get(Config.INTERACTIONS_COMMENTS_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Interactions Comments.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the interactions comments page: {e}",
            )

    def navigate_to_interactions_likes(self):
        """
        Navigates to the interactions likes page of the application.
        """
        try:
            self.driver.get(Config.INTERACTIONS_LIKES_INSTAGRAM)
            log(TAG, LogType.INFO, "Navigated, Instagram Interactions Likes.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while navigating to the interactions likes page: {e}",
            )

    def _scroll_page(self, n=5):
        """
        Scrolls the page n times.
        """
        try:
            for _ in range(n):
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                log(TAG, LogType.INFO, f"Scrolled, {n} times.")
                time.sleep(2)
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while scrolling the page: {e}")

    def _get_post_urls(self):
        """
        Fetches the post URLs from the profile page.
        """
        try:
            _scroll_to_bottom()
            post_elements = driver.find_elements(
                By.XPATH, "//a[contains(@href, '/p/') or contains(@href, '/reel/')]"
            )
            post_urls = [post.get_attribute("href") for post in post_elements]
            log(TAG, LogType.INFO, f"Posts fetched: {len(post_urls)}")
            return post_urls
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while fetching posts: {e}")

    def _scroll_to_bottom(self, pause_time=2):
        """Scrolls to the bottom of the page using Selenium WebDriver.

        Args:
            driver (webdriver): The Selenium WebDriver instance.
            pause_time (int): Time to wait (in seconds) after scrolling to the bottom.
        """
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(pause_time)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_heightelf.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                log(TAG, LogType.INFO, "Scrolled to the bottom.")

        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while scrolling to the bottom: {e}",
            )

    def _scroll_to_login_activity_element(self):
        """
        Scrolls to the login activity element.
        """
        try:
            element = driver.find_element(
                By.XPATH, '//span[text()="Where You\'re Logged in"]'
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("arguments[0].style.border='3px solid red'", element)
            log(TAG, LogType.INFO, "Scrolled to login activity element.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while scrolling to login activity element: {e}",
            )

    def _extract_post_details(self, post_url):
        """
        Extracts the details from a post.
        WARNING: This method only gives the media URL of the first slide of a carousel post.
        """
        try:
            self.driver.get(post_url)
            time.sleep(2)
            username = self._extract_post_username()
            media_url = self._extract_post_media_url()
            time_posted = self._extract_post_time_posted()
            likes = self._extract_post_likes()
            location = self._extract_post_location()
            blue_tick = self._is_post_profile_verified()
            caption = self._extract_post_caption()
            # todo: Extract comments and hashtags
            post_details = {
                "username": username,
                "blue_tick": blue_tick,
                "media_url": media_url,
                "time_posted": time_posted,
                "likes": likes,
                "location": location,
                "caption": caption,
            }

            log(TAG, LogType.INFO, f"Details extracted: {post_details}")
            return post_details
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting details: {e}")

    def _extract_post_username(self):
        """
        Extracts the username from a post.
        """
        try:
            username = driver.find_element(
                By.XPATH,
                '//span[contains(@class, "_ap3a _aaco _aacw _aacx _aad7 _aade")]',
            )
            log(TAG, LogType.INFO, f"Username extracted: {username.text}")
            return username.text
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting username: {e}")
            return None

    def _extract_post_media_url(self):
        """
        Extracts the media from a post.
        Can be either an image or a video.
        Returns:
            str: The URL of the image or BLOB of the video.
        """
        try:
            video_element = driver.find_element(
                By.XPATH, '//video[@class="x1lliihq x5yr21d xh8yej3"]'
            )
            video_url = video_element.get_attribute("src")
            log(TAG, LogType.INFO, f"Media extracted, video: {video_url}")
            return media_url
        except Exception as e:
            image_element = driver.find_element(
                By.XPATH,
                '//img[@class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3"]',
            )
            image_url = image_element.get_attribute("src")
            log(TAG, LogType.INFO, f"Media extracted, image: {image_url}")
            return image_url

    def _extract_post_time_posted(self):
        """
        Extracts the times posted from a post.
        """
        try:
            time_element = driver.find_element(By.XPATH, '//time[@class="x1p4m5qa"]')
            time_posted = time_element.get_attribute("datetime")
            log(TAG, LogType.INFO, f"Time posted: {time_posted}")
            return time_posted
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while extracting time posted: {e}",
            )
            return None

    def _extract_post_likes(self):
        """
        Extracts the number of likes from a post.
        """
        try:
            likes_element = likes = driver.find_element(
                By.XPATH,
                '//span[contains(@class, "xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")]',
            )
            likes = likes_element.text
            log(TAG, LogType.INFO, f"Likes extracted: {likes}")
            return likes
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting likes: {e}")
            return None

    def _extract_post_caption(self):
        """
        Extracts the caption from a post.
        """
        try:
            caption_element = driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')]",
            )
            caption = caption_element.text
            log(TAG, LogType.INFO, f"Caption extracted: {caption}")
            return caption
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting caption: {e}")
            return None

    def _extract_post_location(self):
        """
        Extracts the location from a post.
        """
        try:
            location_element = driver.find_element(
                By.CSS_SELECTOR,
                "a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x5n08af.x9n4tj2._a6hd",
            )
            location = location_element.text
            log(TAG, LogType.INFO, f"Location extracted: {location}")
            return location
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting location: {e}")
            return None

    def _is_post_profile_verified(self):
        """
        Checks if the profile is verified.
        """
        try:
            svg_element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'svg.x1lliihq.x1n2onr6[aria-label="Verified"]')
                )
            )

            if "Verified" == svg_element.get_attribute("aria-label"):
                log(TAG, LogType.INFO, "Profile is verified.")
                return True
            log(TAG, LogType.INFO, "Profile is not verified.")
            return False
        except Exception as e:
            log(TAG, LogType.INFO, "Profile is not verified.")
            return False

    def _click_on_saved_post_container(self):
        """
        Clicks on the saved posts container.
        """
        try:
            span_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[contains(@class, 'x1lliihq') and text()='All posts']",
                    )
                )
            )
            span_element.click()
            log(TAG, LogType.INFO, "Clicked on saved posts container.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while clicking on saved posts container: {e}",
            )

    def _extract_interactions_likes(self):
        """
        Extracts the likes from the interactions page.
        """
        try:
            likes_elements = driver.find_elements(
                By.XPATH,
                "//div[contains(@class, 'x1lliihq x5yr21d xh8yej3')]",
            )
            likes = [like.text for like in likes_elements]
            log(TAG, LogType.INFO, f"Likes extracted: {len(likes)}")
            return likes
        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred while extracting likes: {e}")
            return []

    def _click_on_saved_post_section(self):
        """
        Clicks on the saved posts section.
        """
        try:
            span_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(@class, 'x972fbf') and text()='Saved']")
                )
            )
            span_element.click()
            log(TAG, LogType.INFO, "Clicked on saved posts section.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while clicking on saved posts section: {e}",
            )

    def _click_on_tagged_section(self):
        """
        Clicks on the tagged posts section.
        """
        try:
            span_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[contains(@class, 'x972fbf') and text()='Tagged']",
                    )
                )
            )
            span_element.click()
            log(TAG, LogType.INFO, "Clicked on tagged posts section.")
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while clicking on tagged posts section: {e}",
            )
    
    def _click_on_following_section(self):
        """
        Clicks on the followers section.
        """
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/test_sih_dummy/following/"]'))
            )
            element.click()

        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred: {e}")

    def _click_on_followers_section(self):
        """
        Clicks on the followers section.
        """
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/test_sih_dummy/followers/"]'))
            )
            element.click()

        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred: {e}")

    def _click_on_close_button(self):
        """
        Clicks on the close button in followers/following section.
        """
        try:
            svg_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Close"]'))
            )
            svg_element.click()

        except Exception as e:
            log(TAG, LogType.ERROR, f"An error occurred: {e}")

    def _get_login_details(self):
        """
        Fetches the login details on login activity page from the application.
        """
        data_list = []
        try:
            div_elements = driver.find_elements(
                By.XPATH,
                "//div[contains(@class, 'x1i10hfl') and contains(@class, 'x1qjc9v5')]",
            )
            for div in div_elements:
                span1 = div.find_element(
                    By.XPATH,
                    ".//span[contains(@class, 'x193iq5w') and contains(@class, 'xeuugli') and contains(@class, 'x1fj9vlw')]",
                )
                span2 = div.find_element(
                    By.XPATH,
                    ".//span[contains(@class, 'x193iq5w') and contains(@class, 'xeuugli') and contains(@class, 'x1fj9vlw') and contains(@class, 'x1roi4f4')]",
                )
                location_text = span1.text
                time_os_text = span2.text
                data_dict = {"location": location_text, "time_os": time_os_text}
                data_list.append(data_dict)
            log(TAG, LogType.INFO, f"Login activity fetched: {len(data_list)}")
            return data_list
        except Exception as e:
            print(f"An error occurred: {e}")
            data_list = []
            return data_list

    def _get_location_map(self):
        """
        Fetches the location map from the application.
        Returns:
            list: A list of dictionaries containing the location map urls. {"mid_leaf": str, "right_leaf": str, "left_leaf": str}
        """
        try:
            parent_divs = driver.find_elements(
                By.CSS_SELECTOR,
                "div.x9f619.xjbqb8w.x78zum5.x5ur3kl.xopu45v.x1bs97v6.xmo9t06.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1",
            )
            map_loc = ["mid_leaf", "right_leaf", "left_leaf"]
            login_map = []
            for parent_div in parent_divs:
                try:
                    img_elements = parent_div.find_elements(
                        By.CSS_SELECTOR, "img.leaflet-tile.leaflet-tile-loaded"
                    )
                    if len(img_elements) == 3:
                        map_urls = [img.get_attribute("src") for img in img_elements]
                        mapped_urls = dict(zip(map_loc, map_urls))
                        login_map.append(mapped_urls)
                    else:
                        log(
                            TAG,
                            LogType.WARNING,
                            f"Expected 3 map URLs, but found: {len(img_elements)}",
                        )
                        login_map.append(
                            {"mid_leaf": None, "right_leaf": None, "left_leaf": None}
                        )
                except Exception as e:
                    log(
                        TAG,
                        LogType.ERROR,
                        f"An error occurred while fetching map URLs: {e}",
                    )
            return login_map
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while fetching location map: {e}",
            )
            login_map = []
            return login_map

    def get_followers_names(self):
        """
        Fetches the followers names from the application.
        """
        try:
            self._click_on_followers_section()
            info = []
            parent_divs = driver.find_elements(By.CLASS_NAME, "x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
            for parent_div in parent_divs:
                follower_data = {}
                try:
                    username_element = parent_div.find_element(By.CLASS_NAME, "_ap3a")
                    follower_data['username'] = username_element.text
                except Exception as e:
                    log(TAG, LogType.ERROR, f"An error occurred while fetching followers names: {e}")
                    follower_data['username'] = None

                try:
                    name_element = parent_div.find_element(By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x1roi4f4.x10wh9bi.x1wdrske.x8viiok.x18hxmgj > span.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')
                    follower_data['name'] = name_element.text
                except Exception as e:
                    log(TAG, LogType.ERROR, f"An error occurred while fetching followers names: {e}")
                    follower_data['name'] = None

                info = parent_div.find_element(By.CSS_SELECTOR, 'div._ap3a._aaco._aacw._aad6._aade')
                if info.text in ["Follow", "Requested"]:
                    break
                info.append(follower_data)
            return info
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while fetching followers names: {e}",
            )
            return []

    def get_following_names(self):
        """
        Fetches the following names from the application.
        """
        try:
            self._click_on_following_section()
            info = []
            parent_divs = driver.find_elements(By.CLASS_NAME, "x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
            for parent_div in parent_divs:
                following_data = {}
                try:
                    username_element = parent_div.find_element(By.CLASS_NAME, "_ap3a")
                    following_data['username'] = username_element.text
                except Exception as e:
                    log(TAG, LogType.ERROR, f"An error occurred while fetching following names: {e}")
                    following_data['username'] = None

                try:
                    name_element = parent_div.find_element(By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x1roi4f4.x10wh9bi.x1wdrske.x8viiok.x18hxmgj > span.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')
                    following_data['name'] = name_element.text
                except Exception as e:
                    log(TAG, LogType.ERROR, f"An error occurred while fetching following names: {e}")
                    following_data['name'] = None

                info = parent_div.find_element(By.CSS_SELECTOR, 'div._ap3a._aaco._aacw._aad6._aade')
                if info.text in ["Follow", "Requested"]:
                    break
                info.append(following_data)
            return info
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while fetching following names: {e}",
            )
            return []
            
    def _parse_saved(self):
        """
        Parses the saved posts on profile page of the application.
        """
        self._click_on_saved_post_container()
        self._click_on_saved_post_section()
        post_urls = InstagramService._get_posts_urls()
        post_details_saved = []
        for url in post_urls:
            try:
                info = self._extract_post_details(url)
                post_details_saved.append(info)
            except Exception as _:
                print("\n")
        return post_details_saved

    def _parse_profile(self):
        """
        Parses the posts on profile page of the application.
        """
        post_urls = self._get_posts_urls()
        post_details_profile = []
        for url in post_urls:
            try:
                info = self._extract_post_details(url)
                post_details_profile.append(info)
            except Exception as _:
                print("\n")

        return post_details_profile

    def parse_home(self):
        """
        Parses the home page of the application.
        """
        self.navigate_to_home()
        post_urls = self._get_posts_urls()
        post_details_home = []
        for url in post_urls:
            try:
                info = InstagramService._extract_post_details(url)
                post_details_home.append(info)
            except Exception as _:
                print("\n")
        return post_details_home

    def parse_explore(self):
        """
        Parses the explore page of the application.
        """
        self.navigate_to_explore()
        post_urls = self._get_posts_urls()
        post_details_explore = []
        for url in post_urls:
            try:
                info = self._extract_post_details(url)
                post_details_explore.append(info)
            except Exception as _:
                print("\n")
        return post_details_explore

    def parse_profile(self, user):
        """
        Parses the profile page of the application.
        """
        self.navigate_to_profile(user)
        profile_posts = self._parse_profile()
        tagged_posts = self._parse_tagged()
        saved_posts = self._parse_saved()

        return {"profile": profile_posts, "tagged": tagged_posts, "saved": saved_posts}

    def parse_login_activity(self):
        """
        Fetches the login activity from the application.
        """
        try:
            self.navigate_to_login_activity()
            self._scroll_to_login_activity_element()
            login_activity = self._get_login_details()
            location_map = self._get_location_map()
            login_activity_data = []
            for i in range(len(login_activity)):
                login_activity_data.append({**login_activity[i], **location_map[i]})
            return login_activity_data
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while fetching login activity: {e}",
            )
            login_activity_data = []
            return login_activity_data

    def parse_interactions(self):
        """
        Fetches the interactions from the application.
        """
        try:
            self.navigate_to_interactions_likes()
            interactions = self._get_interactions()
            return interactions
        except Exception as e:
            log(
                TAG,
                LogType.ERROR,
                f"An error occurred while fetching interactions: {e}",
            )
            interactions = []
            return interactions

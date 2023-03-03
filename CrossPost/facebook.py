import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Facebook:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def prompt_login(self):
        username = input("Please enter your Facebook username: ")
        password = input("Please enter your Facebook password: ")
        return username, password

    def login(self, username, password):
        self.driver.get("https://www.facebook.com/")
        # enter login credentials
        email_field = self.driver.find_element_by_id("email")
        email_field.send_keys(username)
        password_field = self.driver.find_element_by_id("pass")
        password_field.send_keys(password)

        # wait for login to complete
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "userNavigationLabel"))
            )
            print("Login successful!")
            return True
        except TimeoutException:
            print("Login failed: invalid credentials")
            choice = input("Would you like to try again? (y/n): ")
            if choice.lower() == "y":
                return self.prompt_login()
            else:
                self.driver.quit()
                return False

    def post_to_facebook(self, data):
        if not self.driver:
            print("Please log in first.")
            return False

        # check if image file exists
        if not os.path.isfile(data["picture_path"]):
            print("Image file not found.")
            return False

        # check if image is too large
        MAX_IMAGE_SIZE = 8_388_608  # 8 MB
        file_size = os.path.getsize(data["picture_path"])
        if file_size > MAX_IMAGE_SIZE:
            print("Image file too large.")
            return False

        # create post
        self.driver.get("https://www.facebook.com/")
        time.sleep(2)
        self.driver.find_element_by_css_selector('[aria-label="Create a post"]').click()
        time.sleep(2)
        self.driver.switch_to.active_element.send_keys(data["text"])
        time.sleep(2)
        add_photo_btn = self.driver.find_element_by_css_selector('[aria-label="Add Photo/Video"]')
        add_photo_btn.click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('input[type="file"]').send_keys(data["picture_path"])
        time.sleep(2)
        self.driver.find_element_by_css_selector('[aria-label="Post"]').click()

        # wait for post to complete
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Your post has been published."]'))
            WebDriverWait(self.driver, 30).until(element_present)
        except:
            print("Post failed.")
            return False

        print("Facebook post complete!")
        return True

    def logout(self):
        if self.driver:
            self.driver.get("https://www.facebook.com/")
            time.sleep(2)
            self.driver.find_element_by_css_selector('[aria-label="Account"]').click()
            time.sleep(2)
            self.driver.find_element_by_css_selector('[aria-label="Log Out"]').click()
            time.sleep(2)
            self.driver.quit()
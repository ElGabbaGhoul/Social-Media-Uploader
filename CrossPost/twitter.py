# this module will be responsible for logging in to twitter, sending out tweets with a photo, some words and a handful of hashtags (optional).

# you are being handed data from main.py. a picture file, and a body of characters. 

# log in to twitter
# submit username and password
    # if fail:
        # print ("Twitter Failed: Unsuccessful Login")
        # break
    # if success:
        # create new tweet with picture file and body of characters
            # if len(body) > len(max)
                # print ("Twitter Failed: Too many Characters")
                # break
            # else
                #send tweet
                # print("Twitter Done")

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self):
        self.driver = None

    def prompt_login(self):
        username = input("Please enter your Twitter username: ")
        password = input("Please enter your Twitter password: ")
        return username, password
    
    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.twitter.com/")

        # enter login credentials
        email_field = self.driver.find_element_by_id("email")
        email_field.send_keys(username)
        password_field = self.driver.find_element_by_id("pass")
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # wait for login to complete
        try:
            element_present = EC.presence_of_element_located((By.ID, "userNavigationLabel"))
            WebDriverWait(self.driver, 10).until(element_present)
        except:
            print("Login failed.")
            self.driver.quit()
            return False

        return True

    def post_to_twitter(self, data):
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
        self.driver.get("https://www.twitter.com/")
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
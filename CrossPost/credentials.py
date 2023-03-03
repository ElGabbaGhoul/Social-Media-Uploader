# stores credentials saved by respective social media 

import keyring

class Credentials:
    def __init__(self):
        self.facebook_username = "your_facebook_username"
        self.facebook_password = "your_facebook_password"
        
        self.twitter_api_key = "your_twitter_api_key"
        self.twitter_api_secret_key = "your_twitter_api_secret_key"
        self.twitter_access_token = "your_twitter_access_token"
        self.twitter_access_token_secret = "your_twitter_access_token_secret"
        
        self.linkedin_client_id = "your_linkedin_client_id"
        self.linkedin_client_secret = "your_linkedin_client_secret"
        self.linkedin_access_token = "your_linkedin_access_token"

    def get_facebook_credentials():
        """
        Prompts the user for their Facebook username and password.
        If the user provides valid credentials, stores the information securely using the keyring library.
        """
        use_facebook = input("Do you want to allow CrossPost to post to Facebook? (y/n): ").lower() == "y"
        if use_facebook:
            fb_username = input("Please enter your Facebook username(email or phone number): ")
            fb_password = input("Please enter your Facebook password: ")
            keyring.set_password("facebook", fb_username, fb_password)
            print("Facebook credentials saved.")

    def get_twitter_credentials():
        """
        Prompts the user for their Twitter username and password.
        If the user provides valid credentials, stores the information securely using the keyring library.
        """
        use_twitter = input("Do you want to allow CrossPost to post to Twitter? (y/n): ").lower() == "y"
        if use_twitter:
            tw_username = input("Please enter your Twitter username (email, phone, or username): ")
            tw_password = input("Please enter your Twitter password: ")
            keyring.set_password("twitter", tw_username, tw_password)
            print("Twitter credentials saved.")

    def get_linkedin_credentials():
        """
        Prompts the user for their LinkedIn username and password.
        If the user provides valid credentials, stores the information securely using the keyring library.
        """
        use_linkedin = input("Do you want to allow CrossPost to post to LinkedIn? (y/n): ").lower() == "y"
        if use_linkedin:
            li_username = input("Please enter your LinkedIn username (email): ")
            li_password = input("Please enter your LinkedIn password: ")
            keyring.set_password("linkedin", li_username, li_password)
            print("LinkedIn credentials saved.")
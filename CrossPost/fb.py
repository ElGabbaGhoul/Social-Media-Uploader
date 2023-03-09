import facebook
import configparser

class FacebookAPI:
    def __init__(self):
      self.config = configparser.ConfigParser()
      self.config.read('config.ini')
      self.graph = None
    
    def login(self):
        app_id = self.config.get('facebook', 'app_id')
        app_secret = self.config.get('facebook', 'app_secret')
        redirect_uri = 'https://localhost/facebook_callback'

        # Use the app credentials to create a new GraphAPI object
        self.graph = facebook.GraphAPI(access_token=None, version='10.0')
        oauth_dialog_url = self.graph.get_auth_url(app_id=app_id, redirect_uri=redirect_uri)
        print(f"Please go to this URL and authorize the application: {oauth_dialog_url}")
        access_token = input("Enter the access token from the URL: ")
        self.graph = facebook.GraphAPI(access_token=access_token, version='10.0')
    
    def post_to_timeline(self, message):
        # Use the Graph API to post a message to the user's timeline
        if self.graph is not None:
            try:
                self.graph.put_object(parent_object='me', connection_name='feed', message=message)
                print("Successfully posted to timeline!")
            except Exception as e:
                print("Post to timeline failed. Error:", e)
        else:
            print("Please login first!")
    
    def logout(self):
        # Clear the access token and graph instance
        self.access_token = None
        self.graph = None
        print("Logged out.")
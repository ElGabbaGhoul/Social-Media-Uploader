# stores credentials saved by respective social media 

import keyring
from fb import FacebookAPI

access_token = keyring.get_password('facebook', 'access_token')
if not access_token:
    access_token = input ('Enter your Facebook access token: ')
    keyring.set_password('facebook', 'access_token', access_token)

fb_api = FacebookAPI(access_token)
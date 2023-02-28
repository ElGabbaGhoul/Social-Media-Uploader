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
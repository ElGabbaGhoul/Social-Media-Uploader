# this module will be responsible for logging in to facebook, sending out posts with a photo, some words and a handful of hashtags (optional).

# you are being handed data from main.py. a picture file, and a body of characters. 

# log in to Facebook
# submit username and password
    # if fail:
        # print ("Facebook Failed: Unsuccessful Login")
        # break
    # if success:
        # create new tweet with picture file and body of characters
            # if len(body) > len(max)
                # print ("Facebook Failed: Too many Characters")
                # break
            # else
                #send tweet
                # print("Facebook Done")
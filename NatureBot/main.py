# this file will be responsible for handling the logic of asking for a photo, a message, and some optional hashtags.

# greet user
# present TOS. This is for pictures of nature only and using the tool to break TOS is bad.
    # if user disagree
        # break
    # else
        # ask for photo (navigate to submissions folder and select photo)
        # ask for body 5-500 char
        # ask for hashtags(optional)
            # break up individual words broken by commas, add a # before each word, append to body.
        # JSONify? hand it off to the functions of the other social media modules. they handle the upload. 
        # Thank you message
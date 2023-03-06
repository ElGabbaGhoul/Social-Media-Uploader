## a journal to keep track of progress ##

## WorkFlow ##

 ## update journal on main 
 ## choose branch
 ## finish branch
 ## start on new branch
 ## when all branches are finished and main is up to date, flesh out readme. 
    give good instructions on how to use this program. 
    give out the Repo. 
    Make a YouTube video. 
    have people test it and try to break it. 
    add other platforms. 
    the possibilities are endless.
    Keep going!

02/27/23
Project NatureBot Created
    - created idea for The Project. Input a picture of Nature. Woods, trees, flowers, animals, etc etc., along with a description of the picture, some hashtags, and then send that out to all linked social media platforms. At this time, the desired platforms are Facebook, Twitter, Instagram, LinkedIn. 
    - Found out that Instagram's API is no longer very good, or even possible to work with. 
    - Decided I should make a new Facebook account for project NatureBot.


02/28/23
    - At this time the desired platforms for which The Project are to be integrated with are LinkedIn, Facebook, and Twitter.
    - I will not be creating any new accounts.
    - began UI layout planning. Mind mapping, flowcharting, etc. in Figma, Excalidraw and similar softwares.    
    - Except not really lol. 
    - Pseudocoding out basic functionality of each module and main.py. 
    - Testing ideas with basic code from CGPT

03/2/23
    - began implementing facebook api communication to allow content to post.
    - decided CrossPost is a better name for this app, as it doesn't limit user to one kind of image. 
    - did a lot of work on things besides facebook on facebook branch
    - added facebook (and twitter) post submission functionality
    - added credentials.py which saves hashed passwords. allegedly. 

    - FOR TOMORROW: I am going to have credentials be the module that asks what platform the user wants to post to. then the request for credentials will come from the respective module. Currently, credentials asks, as does the Social Media Platform Module (SMPP). Keep up the good work scooter C:

03/03/23
    - facebook branch contains way more than facebook stuff. That's ok. It's all on main, and when we work on the branches in the future, we'll just edit the crap out. 
    - established workflow conducive to getting good stuff done. 
    - continued implementing Facebook branch functionality.
    - began to chart out flow on miro.
    - plotted out flow on miro

    - still need to add main.py: initialize replies as empty list, add query function, then add logic re replies. 
    - pl
    - Plans for 03/06/23
        - compare extensions between vscode on laptop and vscode on pc. look for function paragraph identifier. whatever it's called.
        - gui sounds easy. maybe plan it out on miro since it looks like the planning will take longer than implementing. can plan it out before coding more for the backend. backend is basically planned out, just need to fine tune the ordering of functions in main.py and add login functionality for twitter and linkedin. 
        - During testing and development, I will be interacting with CrossPost via input() and responding in the terminal.
            - steps for data flow is as follows:
                - user opens program for the first time after installing 
                - hello - welcome to crosspost. would you like to post to facebook? Linkedin? Twitter? 
                - user answers yes or no
                - program remembers answers
                - for each approved platform, user enters relevant login info
                - login information is saved, hashed, secured, etc etc. 
                - program requests user to prepare a post, post must be at least 1 picture, text body 5 character minimum, hashtags optional
                - user provides proper data, can post!
                - program sends posts to approved sites. show progress and status (=====-----) 50% ~
                - see your post? program gets url for post. presents it to user.
        - when this application has a gui, I will be allowing them to save their login information locally. it will be hashed and secure. 
        - this is a good idea but will require much brainpower. don't smoke in the morning. you can smoke after work. 6pm. 
        - also need to work on portfolio, jampackd, and krys' portfolio. schedule a meeting with them on Monday, 3/6. 
        - send at least 20 job apps out this week. 
from fb import FacebookAPI
# import tkinter as tk
# import tkinter.filedialog as fd

# function to query which platforms app can post to.
platforms = ["Facebook", "LinkedIn", "Twitter"]
def query_platforms(platforms):
  # initialize responses list
  responses = []

  for p in platforms:
    response = input(f"Would you like CrossPost to post to {p}? (yes/no): ")
    if response.lower() == 'yes':
      responses.append(p[:2].lower())
  return responses

responses = query_platforms(platforms)
print(responses)







# def create_post():
#     root = tk.Tk()
#     root.withdraw()

#     # prompt user for text submission
#     text_submission = input("Please enter your text submission (5-256 characters): ")
#     while len(text_submission) < 5 or len(text_submission) > 256:
#         text_submission = input("Please enter your text submission (5-256 characters): ")

#     # prompt user for hashtags
#     add_hashtags = input("Do you want to add hashtags? (Y/N): ")
#     while add_hashtags not in ["Y", "N"]:
#         add_hashtags = input("Do you want to add hashtags? (Y/N): ")

#     hashtags = ""
#     if add_hashtags == "Y":
#         hashtags_input = input("Please enter your hashtags (comma separated): ")
#         hashtags_list = hashtags_input.split(",")
#         for tag in hashtags_list:
#             hashtags += "#" + tag.strip().lower() + " "

#     # prompt user to select a picture
#     pic_folder_path = "./CrossPost/pics"
#     pic_filetypes = [("JPEG files", "*.jpg"), ("PNG files", "*.png")]
#     pic_filename = fd.askopenfilename(initialdir=pic_folder_path, title="Select Picture", filetypes=pic_filetypes)

#     if not pic_filename:
#         print("No picture selected. Exiting.")
#         return

#     # prepare data to hand off to another module
#     data = {
#         "text": text_submission + " " + hashtags,
#         "picture_path": pic_filename
#     }
#     print("\nSUCCESS!! DATA TO BE SENT TO SOCIAL MEDIA PLATFORMS HERE! \n", "Data:", data)

# # prompt user for post data
# data = create_post()

# # log in to Facebook
# fb = Facebook
# username, password = fb.prompt_login()
# fb.login(username, password)

# # post to Facebook
# fb.post_to_facebook(data)

# # log out
# fb.logout()

#log in to twitter
# tw = Twitter
# username, password = tw.prompt_login()
# tw.login(username, password)

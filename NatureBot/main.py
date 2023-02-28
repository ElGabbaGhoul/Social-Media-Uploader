import os
import tkinter as tk
import tkinter.filedialog as fd
import win32gui
import win32con

def create_post():
    root = tk.Tk()
    root.withdraw()

    # prompt user for text submission
    text_submission = input("Please enter your text submission (5-256 characters): ")
    while len(text_submission) < 5 or len(text_submission) > 256:
        text_submission = input("Please enter your text submission (5-256 characters): ")

    # prompt user for hashtags
    add_hashtags = input("Do you want to add hashtags? (Y/N): ")
    while add_hashtags not in ["Y", "N"]:
        add_hashtags = input("Do you want to add hashtags? (Y/N): ")

    hashtags = ""
    if add_hashtags == "Y":
        hashtags_input = input("Please enter your hashtags (comma separated): ")
        hashtags_list = hashtags_input.split(",")
        for tag in hashtags_list:
            hashtags += "#" + tag.strip().lower() + " "

    # prompt user to select a picture
    pic_folder_path = "pics"
    pic_filetypes = [("JPEG files", "*.jpg"), ("PNG files", "*.png")]
    pic_filename = fd.askopenfilename(initialdir=pic_folder_path, title="Select Picture", filetypes=pic_filetypes)

    if not pic_filename:
        print("No picture selected. Exiting.")
        return

    # prepare data to hand off to another module
    data = {
        "text": text_submission + " " + hashtags,
        "picture_path": pic_filename
    }
    print("Data:", data)

    # bring picture window to the foreground
    pic_window = win32gui.FindWindow(None, "Select Picture")
    win32gui.SetForegroundWindow(pic_window)

create_post()

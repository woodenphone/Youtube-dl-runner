#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      new
#
# Created:     26/12/2013
# Copyright:   (c) new 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import subprocess
import sys
import time
import Tkinter


def read_clipboard():
    # http://stackoverflow.com/questions/7881230/copy-data-from-the-clipboard-on-linux-mac-and-windows-with-a-single-python-scri?rq=1
    root = Tkinter.Tk()
    root.withdraw() # Hide the main window (optional)
    text_in_clipboard = root.clipboard_get()
    return text_in_clipboard



def update():
    """Try to update youtube-dl.exe"""
    print "Attempting to update...."
    program_location = sys.executable
    program_name = "youtube-dl.exe"
    update_arg = "--update"
    command = [program_name, update_arg]
    result = subprocess.call(command)
    print "Command result: ", result
    time.sleep(5)
    print "Finished updating."


def download(target_url):
    """Do downloads using youtube-dl.exe"""
    program_location = sys.executable
    program_name = "youtube-dl.exe"
    # Define arguments. see this url for help
    # https://github.com/rg3/youtube-dl
    ignore_errors = "-i"
    safe_filenames = "--restrict-filenames"
    output_arg = "-o"
    output_template = "download\%(uploader)s\%(playlist)s\%(title)s-%(id)s.%(ext)s"
    command = [program_name, ignore_errors, safe_filenames, output_arg, output_template, target_url]
    result = subprocess.call(command)
    print "Command result: ", result






def user_interface():
    while True:
        print ""
        print ""
        print "Enter target URL"
        print "Leave blank to read clipboard. Enter x to exit."
        target_url = raw_input("")
        if target_url == "":
            target_url = read_clipboard()
            print "Read from clipboard:", target_url
        elif target_url == "x":
            return
        download(target_url)


def main():
    update()
    user_interface()
    raw_input("Press return to exit.")

if __name__ == '__main__':
    main()

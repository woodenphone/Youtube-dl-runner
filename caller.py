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


def update():
    """Try to update youtube-dl.exe"""
    print "Attempting to update...."
    program_location = sys.executable
    program_name = "youtube-dl.exe"
    update_arg = "--update"
    command = [program_name, update_arg]
    result = subprocess.call(command)
    print "Command result: ", result
    print "Finished updating."


def download():
    """Do downloads using youtube-dl.exe"""
    program_location = sys.executable
    program_name = "youtube-dl.exe"
    ignore_errors = "-i"
    safe_filenames = "--restrict-filenames"
    output_arg = "-o"
    output_template = "download\%(uploader)s\%(playlist)s\%(title)s-%(id)s.%(ext)s"
    target_url = None
    while target_url is not "":
        target_url = raw_input("Enter target URL")
        command = [program_name, ignore_errors, safe_filenames, output_arg, output_template, target_url]
        result = subprocess.call(command)
        print "Command result: ", result
        print ""
        print ""



def main():
    update()
    download()
    raw_input("Press return to exit.")

if __name__ == '__main__':
    main()

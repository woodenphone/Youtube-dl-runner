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




program_location = sys.executable
program_name = "youtube-dl.exe"
ignore_errors = "-i"
safe_filenames = "--restrict-filenames"
output_arg = "-o"
output_template = "%(uploader)s\%(playlist)s\%(title)s-%(id)s.%(ext)s"
target_url = raw_input("Enter target URL")

command = [program_name, ignore_errors, safe_filenames, output_arg, output_template, target_url]
result = subprocess.call(command)
print "Command result: ", result

raw_input("Press return to exit.")

def main():
    pass

if __name__ == '__main__':
    main()

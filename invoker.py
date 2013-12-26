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

import youtube_dl

downloader_args = {
    "ignoreerrors" : True,
    "outtmpl" : "%(uploader)s\%(playlist)s\%(title)s-%(id)s.%(ext)s"

}

downloader = youtube_dl.YoutubeDL(downloader_args)




target_url = "https://www.youtube.com/playlist?list=PL-XXv-cvA_iBTE0TyTr1MXaoihYpqPhwc"

result = downloader.extract_info(target_url)




raw_input("")
def main():
    pass

if __name__ == '__main__':
    main()

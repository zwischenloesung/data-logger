#!/usr/bin/python
#########################################################################
# Dispatch different file uploads
#########################################################################
# Just used for testing..
#########################################################################

import os
import cgi
import datetime
import re

# debug {{ #
#import cgitb
#cgitb.enable(display=0, logdir="/path/logfile")
# debug }} #

def store(storage_path, data):
    try:
        if ctype == 'multipart/form-data':
            self.send_header("Content-type", "text/plain")
            print data.value.__repr__()
        elif ctype == 'application/xml':
            file_content = data.value.__repr__()
            print file_content
            file_content = file_content.strip("'")
            file_content = file_content.strip('"')
            file_content = re.sub("\\\\r", "", file_content)
            file_content = re.sub("\\\\n", "\n", file_content)
            with open(outfile, "w") as of:
                of.write(file_content)
        self.send_response(200)
        self.end_headers()
    except:
        print("Error: no data received...")
        self.send_response(500)
        self.end_headers()

if __name__ == "__main__":

    storage_path = "/tmp/"

    print "Content-Type: text/plain;charset=utf-8"
    print ""
    print "Start uploading.."
    data = cgi.FieldStorage()
    store(storage_path, data)
    print "..done!"


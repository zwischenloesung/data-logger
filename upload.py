#!/usr/bin/python

import os
import commands
import cgi
import datetime
import re
import sys

#import cgitb
#cgitb.enable(display=0, logdir="/path/logfile")

file_latest = "latest"
connection_file_suffix="txt"
connection_file_path = "/srv/www/data/connection"
data_file_suffix = "xml"
data_file_path = "/srv/www/data/sensor-data"
file_upload_key = "file"

print "Content-Type: text/plain;charset=utf-8"
print ""
print "Start uploading.."

data = cgi.FieldStorage()

timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
connection_file = connection_file_path + "-" + file_latest + "." + \
    connection_file_suffix
data_file = data_file_path + "-" + file_latest + "." + data_file_suffix
data_archive = data_file_path + "-" + timestamp + "." + data_file_suffix

try:
    with open(connection_file, "w") as of:
        for i in data.keys():
            of.write(i + ": " + data[i].value + "; ")
    fh = data[file_upload_key]
    if fh.file:
        l = fh.file.read()
        with open(data_file, "w") as of:
            of.write(l)
        with open(data_archive, "w") as of:
            of.write(l)
except TypeError, KeyError:
    file_content = data.value.__repr__()
    file_content = file_content.strip("'")
    file_content = file_content.strip('"')
    file_content = re.sub("\\\\r", "", file_content)
    file_content = re.sub("\\\\n", "\n", file_content)
    with open(data_file, "w") as of:
        of.write(file_content)
    with open(data_archive, "w") as of:
        of.write(file_content)

print "..done!"


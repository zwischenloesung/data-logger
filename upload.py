#!/usr/bin/python

import os
import commands
import cgi
#import cgitb
#cgitb.enable(display=0, logdir="/path/logfile")

print "Content-Type: text/plain;charset=utf-8"
print ""
print "Start uploading.."
data = cgi.FieldStorage()

for k in data.keys():
    print i + ": " + form[i].value + "; "

fh = form['upload']
if fh.file:
    with file("/srv/www/data/sensor-data-latest.xml", 'w') as outfile:
        outfile.write(fh.file.read())

print "..done!"


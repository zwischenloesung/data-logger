#!/usr/bin/python

import os
import cgi
import datetime
import re

# debug {{ #
#import cgitb
#cgitb.enable(display=0, logdir="/path/logfile")
# debug }} #

def store(storage_path):
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
    file_latest = "latest"
    connection_file_suffix = "txt"
    data_file_suffix = "xml"
    file_upload_key = "file"
    connection_file = storage_path + "connection-" + file_latest + "." + \
                                        connection_file_suffix
    data_file = storage_path + "sensor-data-" + file_latest + "." + \
                                        data_file_suffix
    data_archive = storage_path + "sensor-data-" + timestamp + "." + \
                                        data_file_suffix
    data = cgi.FieldStorage()
    try:
        # if the data is sent as structured data, access it via key
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
        # if the data is contained directly in the content, extract it
        file_content = data.value.__repr__()
        file_content = file_content.strip("'")
        file_content = file_content.strip('"')
        file_content = re.sub("\\\\r", "", file_content)
        file_content = re.sub("\\\\n", "\n", file_content)
        with open(data_file, "w") as of:
            of.write(file_content)
        with open(data_archive, "w") as of:
            of.write(file_content)

if __name__ == "__main__":

    storage_path = "/srv/www/data/"

    print "Content-Type: text/plain;charset=utf-8"
    print ""
    print "Start uploading.."
    store(storage_path)
    print "..done!"


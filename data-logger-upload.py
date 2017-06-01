#!/usr/bin/python

# Script for a certain data-logger..

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

    data_file = storage_path + "sensor-data-latest.xml"
#    data_archive = storage_path + "sensor-data-" + timestamp + ".xml"

    repl = 'Content-Type: application/xml;charset=iso-8859-1\n\n' + \
            '<?xml version="1.0" encoding="iso-8859-1"?>\n' + \
            '<Response responseTime="' + timestamp + '" hascmds="false">\n'

    data = cgi.FieldStorage() 
    try:
        file_content = data.value.__repr__()
        file_content = file_content.strip("'")
        file_content = file_content.strip('"')
        file_content = re.sub("\\\\r", "", file_content)
        file_content = re.sub("\\\\n", "\n", file_content)
        with open(data_file, "w") as of:
            of.write(file_content)
#        with open(data_archive, "w") as of:
#            of.write(file_content)
        repl += ' <Ack status="OK"></Ack>\n' + '</Response>\n'
        print repl
    except:
        repl += ' <Ack status="FAIL">Error</Ack>\n' + '</Response>\n'
        print repl

if __name__ == "__main__":

    store("/tmp")


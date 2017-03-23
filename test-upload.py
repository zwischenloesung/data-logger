#!/usr/bin/python

# This is a testing script that simulates a device:
# We get data from a device as POST Request. The data is directly
# streamed without a form.

from base64 import b64encode
import getpass
import httplib
import requests
import sys
import urllib2

def upload(url, do_verify=True):
    try:
        payload = "<?xml version='1.0' encoding='utf-8' ?>\n<foobar>TEST</foobar>"
        print "User: "
        user = sys.stdin.readline().rstrip()
        password = ""
        if (user):
            password = getpass.getpass()
            credentials = b64encode(user + ":" + password).decode("ascii")
        if password:
            headers = {"Content-Type": "application/xml", 'Authorization': 'Basic %s' %  credentials}
        else:
            headers = {"Content-Type": "application/xml"}
        request = requests.post(url, headers=headers, data=payload, verify=do_verify)
    except httplib.IncompleteRead as e:
        request = e.partial

    print(request.text)
    return request

if __name__ == '__main__':

    try:
        url = sys.argv[1]
    except:
        print "usage: test-upload.py [option] url"
        quit()

    do_verify = True
    if ((url == "-h") or (url == "--help")):
        print "usage: test-upload.py [option] url"
        print "                      -h|--help     print this help"
        print "                      -i|--insecure do not verify certificate"
        quit()
    elif (url == "-i"):
        url = sys.argv
        do_verify = False
    upload(url, do_verify)


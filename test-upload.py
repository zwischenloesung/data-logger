#!/usr/bin/python

# test-upload.py url

from base64 import b64encode
import getpass
import httplib
import requests
import sys
import urllib2

def upload(url):
    try:
        print "User: "
        user = sys.stdin.readline().rstrip()
        password = getpass.getpass()
        credentials = b64encode(user + ":" + password).decode("ascii")
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "'<xml><foo/></xml>'", 'Authorization': 'Basic %s' %  credentials}
        request = requests.get(url, headers=headers, verify=False)
    except httplib.IncompleteRead as e:

        request = e.partial

    print(request.text)
    return request

if __name__ == '__main__':

    url = sys.argv[1]
    upload(url)


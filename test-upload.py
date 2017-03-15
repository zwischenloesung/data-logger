#!/usr/bin/python

# test-upload.py url

import sys
import urllib2
import requests
import httplib

def upload(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "'<xml><foo/></xml>'"}
        request = requests.get(url, headers=headers, verify=false)
    except httplib.IncompleteRead as e:

        request = e.partial

    print(request.text)
    return request

if __name__ == '__main__':

    url = sys.argv[1]
    upload(url)


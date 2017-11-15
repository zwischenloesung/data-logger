#!/usr/bin/env python
#########################################################################
# Test HTTP Server
#########################################################################
# Just used for testing..
#########################################################################

import BaseHTTPServer
import cgi
import re
import sys

class DataLogRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

def httpd(socketaddress, handler=DataLogRequestHandler):
    try:
        s = BaseHTTPServer.HTTPServer(socketaddress, handler)
        print "Server started"
        s.serve_forever()
    except KeyboardInterrupt:
        s.socket.close()

def setup():
    try:
        print "Server IP [127.0.0.1]: "
        a = sys.stdin.readline().rstrip()
        if not a:
            a = "127.0.0.1"
        print "Server Port [8000]: "
        p = sys.stdin.readline().rstrip()
        if not p:
            p = 8000
        socketaddress = (a, int(p))
    except:
        quit()
    return socketaddress

if __name__ == "__main__":
    httpd(setup())



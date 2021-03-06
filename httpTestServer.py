#!/usr/bin/env python
#########################################################################
# Test HTTP Server
#########################################################################
# Just used for testing..
#########################################################################

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
import datetime
import re
import sys
import upload_dispatcher
import urlparse

class DataStoreRequestHandler(BaseHTTPRequestHandler, object):
    def __init__(self, *arg):
        self.out_path = "/tmp"
        self.in_path = "."
        super(DataStoreRequestHandler, self).__init__(*arg)

    def do_GET(self):
#        timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
        if len(self.path) <= 1:
            self.path = "/index.html"
        html_path = "./" + self.path
        with open(html_path, "r") as of:
            html = of.read()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(html)
        return

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        data = cgi.FieldStorage()
        try:
            upload_dispatcher.store(self.out_path, data)
        except:
            print("Error: Server Error...")
            self.send_response(500)
            self.end_headers()

def httpd(socketaddress, handler=DataStoreRequestHandler):
    try:
        s = HTTPServer(socketaddress, handler)
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



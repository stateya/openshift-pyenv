#! /usr/bin/env python

import sys
import os

serve_addr = (os.environ['OPENSHIFT_DIY_IP'], int(os.environ['OPENSHIFT_DIY_PORT']))
if sys.version_info < (3, 0, 0):
    import socketserver
    from BaseHTTPServer import BaseHTTPRequestHandler
else:
    from http.server import BaseHTTPRequestHandler
    import socketserver

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'hello')
        return

Handler = GetHandler
print("serving at port", serve_addr)
httpd = socketserver.TCPServer(serve_addr, Handler)
httpd.allow_reuse_address = True
httpd.serve_forever()

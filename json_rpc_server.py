# coding=utf-8

from __future__ import print_function

import logging
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

from jsonrpc import JSONRPCResponseManager, dispatcher

from MSISDN import Parser

logging.basicConfig(level=logging.DEBUG)

dispatcher.add_class(Parser)


class Handler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('Handler')
        self.logger.debug('__init__')
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        self.logger.debug('do_POST')
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        response = JSONRPCResponseManager.handle(post_body, dispatcher)
        self.wfile.write(response.json)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == '__main__':
    address = ('localhost', 9000)
    server = ThreadedHTTPServer(address, Handler, bind_and_activate=False)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.server_bind()
    server.server_activate()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
    server.server_close()

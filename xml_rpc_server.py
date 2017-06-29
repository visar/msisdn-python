# coding=utf-8

from __future__ import print_function

import logging
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCServer
from xml.etree.ElementTree import Element

from MSISDN import Parser

# Set up logging
logging.basicConfig(level=logging.DEBUG)


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class InstanceParser(Parser):
    def _dispatch(self, method, args):
        try:
            result = getattr(self, method)(*args)
            elem = Element(tag='msisdn')
            for key, val in result.items():
                child = Element(key)
                child.text = str(val)
                elem.append(child)

            return elem
        except Exception as e:
            elem = Element(tag='error')
            child = Element('message')
            child.text = e.message
            elem.append(child)
            return elem


server = SimpleXMLRPCServer(('localhost', 9000),
                            logRequests=True,
                            requestHandler=RequestHandler)

server.register_introspection_functions()
server.register_instance(InstanceParser())

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')

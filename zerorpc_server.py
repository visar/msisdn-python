# coding=utf-8

from __future__ import print_function

import logging

import zerorpc

from MSISDN import Parser

# Set up logging
logging.basicConfig(level=logging.DEBUG)


class InstanceParser(Parser):
    def __init__(self):
        self.logger = logging.getLogger('Parser')

    def transform(self, msisdn):
        try:
            result = Parser.transform(msisdn)
            self.logger.debug(result)
            return result
        except Exception as e:
            self.logger.debug(e.message)
            return e.message


server = zerorpc.Server(InstanceParser())
server.bind('tcp://0.0.0.0:9000')

try:
    server.run()
except KeyboardInterrupt:
    print('Exiting')

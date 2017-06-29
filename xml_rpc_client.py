# coding=utf-8

from __future__ import print_function

import sys
import xmlrpclib


def main():
    proxy = xmlrpclib.ServerProxy('http://localhost:9000')

    if len(sys.argv) > 1:
        try:
            result = proxy.transform(sys.argv[1])
            print(result)
        except Exception as e:
            print(e)
    else:
        print(proxy.transform('+38976123456'))


if __name__ == '__main__':
    main()

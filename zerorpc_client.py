# coding=utf-8

from __future__ import print_function

import sys

import zerorpc


def main():
    client = zerorpc.Client()
    client.connect('tcp://127.0.0.1:9000')

    if len(sys.argv) > 1:
        try:
            result = client.transform(sys.argv[1])
            print(result)
        except Exception as e:
            print(e)
    else:
        print(client.transform('+38976123456'))


if __name__ == '__main__':
    main()

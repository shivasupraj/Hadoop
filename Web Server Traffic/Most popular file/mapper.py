#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        path = data[6].replace('http://www.the-associates.co.uk','')
        print "{0}\t{1}".format(path, 1)

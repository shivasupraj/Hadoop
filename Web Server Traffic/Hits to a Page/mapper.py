#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        request = data[6]
        print "{0}\t{1}".format(request, 1)

#!/usr/bin/python

import sys
count = 0
salesTotal = 0
for line in sys.stdin:
    key, val = line.strip().split()
    count += float(key)
    salesTotal += float(val)

print count,"\t",salesTotal

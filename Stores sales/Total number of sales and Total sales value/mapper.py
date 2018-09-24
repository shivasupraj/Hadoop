#!/usr/bin/python

import sys

count = 0
totalSales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        count += 1
        totalSales += float(cost)

print "{0}\t{1}".format(count, totalSales)

#!/usr/bin/python

import sys
oldFile = None
count = 0
for line in sys.stdin:
    thisFile,thisVal = line.strip().split()
    if oldFile and oldFile != thisFile:
        print "{0}\t{1}".format(oldFile, count)
        count = 0

    oldFile = thisFile
    count += 1

if oldFile:
    print "{0}\t{1}".format(oldFile, count)

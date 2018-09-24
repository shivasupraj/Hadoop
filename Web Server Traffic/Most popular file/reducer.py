#!/usr/bin/python

import sys
maxFile = None
oldFile = None
count = 0
maxCount = 0

for line in sys.stdin:
    thisFile, key  = line.split('\t')
    if oldFile and oldFile != thisFile:
        if maxCount < count:
          maxFile = oldFile
          maxCount = count
        #print oldFile, count
        #print maxFile, maxCount
        count = 0
    oldFile = thisFile
    count += int(key)

if maxCount < count:
    maxFile = thisFile
    maxCount = count
if maxFile:
    print "{0}\t{1}".format(maxFile, maxCount)

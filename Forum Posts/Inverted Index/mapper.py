#!/usr/bin/python

import sys
import csv
delimeters = '.,!?:;"()<>[]#$=-/'

reader = csv.reader(sys.stdin,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t')
for line in reader:
    data = line
    if len(data) == 19:
       node_id = data[0]
       body = data[4]
       for delim in delimeters:
           body = body.replace(delim, ' ')
       words = body.split()
       for word in words:
           print '{0}\t{1}'.format(word.lower(), node_id)
           

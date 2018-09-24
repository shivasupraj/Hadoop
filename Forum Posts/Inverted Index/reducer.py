#!/usr/bin/python

import sys

node_id_list = []
oldWord = None
for line in sys.stdin:
    thisWord, node_id = line.strip().split('\t')
    if oldWord and thisWord != oldWord:
        print '{0}\t{1}\t{2}'.format(oldWord, node_id_list, len(node_id_list))
	node_id_list = []
    oldWord = thisWord
    node_id_list.append(node_id)

if oldWord:
    print '{0}\t{1}\t{2}'.format(oldWord, node_id_list, len(node_id_list))

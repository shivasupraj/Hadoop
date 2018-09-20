#!/usr/bin/python

import sys

oldStore = None
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisStore, thisStoreCost = data_mapped

	if oldStore and oldStore == thisStore:
		oldStoreCost =  max(oldStoreCost, float(thisStoreCost))
		continue
	elif oldStore and oldStore != thisStore:
		print oldStore, "\t", oldStoreCost
	oldStore = thisStore
	oldStoreCost = float(thisStoreCost)

if oldStore:
	print  oldStore, "\t", oldStoreCost

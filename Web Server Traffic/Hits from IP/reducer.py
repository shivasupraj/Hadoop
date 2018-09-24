#!/usr/bin/python

import sys

old_ip_addr = None
count = 0
for line in sys.stdin:
    ip_addr, val = line.strip().split()
    if old_ip_addr and old_ip_addr != ip_addr:
        print "{0}\t{1}".format(old_ip_addr, count)
        count = 0
    old_ip_addr = ip_addr
    count += 1

if old_ip_addr:
    print "{0}\t{1}".format(old_ip_addr, count)

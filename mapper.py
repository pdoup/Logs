#!/usr/bin/python3

from sys import stdin as input_stream

for line in input_stream:
    ip, date, time = line.strip().split(',')[:3]
    print ("%s,%s,%s" %(ip,date,time))

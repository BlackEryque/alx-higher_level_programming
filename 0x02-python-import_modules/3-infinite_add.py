#!/usr/bin/python3
import sys

length = len(sys.argv)
total = 0

if (length - 1) == 0:
    print("0")
else:
    i = 1
    while (i < length):
        x = int(sys.argv[i])
        total += x
        i = i + 1
print("{}".format(total))

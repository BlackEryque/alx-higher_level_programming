#!/usr/bin/python3
import sys

num_elmts = len(sys.argv)

if (num_elmts - 1) == 0:
    print("{} arguements.".format(num_elmts - 1))
else:
    print("{} arguements:".format(num_elmts))
    for i in range(1, num_elmts):
        print("{}: {}".format(i, sys.argv[i]))

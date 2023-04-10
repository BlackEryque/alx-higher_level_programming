#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_elmts = len(sys.argv)

    if (num_elmts - 1) == 0:
        print("{} arguments.".format(num_elmts - 1))
    elif (num_elmts - 1) == 1:
        print("{} argument:".format(num_elmts - 1))
        for i in range(1, num_elmts):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(num_elmts - 1))
        for i in range(1, num_elmts):
            print("{}: {}".format(i, sys.argv[i]))

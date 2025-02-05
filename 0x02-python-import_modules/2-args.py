#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argumentStr = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argumentStr += 's.'
elif argc == 1:
    argumentStr += ':'
else:
    argumentStr += 's:'
print(argumentStr.format(argc))

for i, argument in enumerate(sys.argv):
    if i != 0:
        print("{:d}: {:s}".format(i, argument))

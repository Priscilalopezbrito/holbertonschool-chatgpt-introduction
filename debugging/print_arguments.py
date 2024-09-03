#!/usr/bin/python3
import sys
import os

print(os.path.basename(sys.argv[0]))

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

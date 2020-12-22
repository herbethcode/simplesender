#!/usr/bin/python3

import platform
import sys

vr  = platform.python_version().split('.')[0]
if int(vr) == 2:
    sys.exit("Sorry this script requires python 3.x")

from simplesender import main

if __name__ == '__main__':
    main.run()

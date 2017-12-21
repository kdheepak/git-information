#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from subprocess import call
import shlex
import time


if __name__ == '__main__':
    try:
        folder = sys.argv[1]
    except:
        folder = '.'

    try:
        call("clear")
        while True:
            call(shlex.split("tree {folder}".format(folder=folder)))
            time.sleep(1)
            call("clear")
    except KeyboardInterrupt:
        pass

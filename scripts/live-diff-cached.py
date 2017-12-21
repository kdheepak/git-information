#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
import shlex
import time


if __name__ == '__main__':
    try:
        call("clear")
        while True:
            call(shlex.split("git --no-pager diff --cached"))
            time.sleep(1)
            call("clear")
    except KeyboardInterrupt:
        pass

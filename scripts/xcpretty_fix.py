#!/usr/bin/env /usr/bin/python

import sys
import re

has_undefined = False
while True:
    line = sys.stdin.readline()
    if line == "":
        break
    if line.startswith("Undefined symbols"):
        has_undefined = True
    elif has_undefined and not line.startswith("  "):
        has_undefined = False
    if has_undefined:
        line = "ld: " + line
    print(line)
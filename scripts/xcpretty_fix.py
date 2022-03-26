#!/usr/bin/env python

import sys
import re

has_undefined = False
while True:
    line = sys.stdin.readline()
    if len(line) == 0:
        break
    if line.startswith("Undefined symbols") or has_undefined:
        has_undefined = True
        line = line.replace("Undefined symbols", "ld: Undefined symbols")
        line = re.sub(r'(.*, referenced from:)', r'ld: \1', line)
        line = re.sub(r'(.* in .*\(.*\.o\))', r'ld: \1', line)
    print(line)
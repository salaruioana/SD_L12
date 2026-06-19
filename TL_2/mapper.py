#!/usr/bin/env python3
import sys
import re

pattern = sys.argv[1]

for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(f"match\t{line}")
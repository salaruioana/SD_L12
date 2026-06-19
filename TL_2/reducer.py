#!/usr/bin/env python3
import sys

for line in sys.stdin:
    _, text = line.split("\t", 1)
    print(text)
#!/usr/bin/env python3
import sys

current_key = None
words = []

for line in sys.stdin:
    line = line.strip()
    key, word = line.split("\t")

    if current_key != key:
        if current_key is not None:
            print(f"{current_key}\t{words}")
        current_key = key
        words = []

    words.append(word)

if current_key is not None:
    print(f"{current_key}\t{words}")
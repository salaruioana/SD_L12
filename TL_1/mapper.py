import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        if word:
            key = word[0].lower()
            print(f"{key}\t{word}")
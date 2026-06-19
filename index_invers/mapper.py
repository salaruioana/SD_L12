#!/usr/bin/env python3

import sys
from collections import defaultdict

current_word = None
docs = defaultdict(int)

for line in sys.stdin:
    word, document = line.strip().split('\t')

    if current_word is None:
        current_word = word

    if word != current_word:

        postings = ", ".join(
            f"{doc}: {count}"
            for doc, count in sorted(docs.items())
        )

        print(f"{current_word}\t{{{postings}}}")

        current_word = word
        docs = defaultdict(int)

    docs[document] += 1

if current_word is not None:
    postings = ", ".join(
        f"{doc}: {count}"
        for doc, count in sorted(docs.items())
    )

    print(f"{current_word}\t{{{postings}}}")

# in terminal chmod +x reducer.py


# for f in docs/*.txt
# do
#     export map_input_file=$(basename "$f")
#     cat "$f" | ./mapper.py
# done > mapped.txt

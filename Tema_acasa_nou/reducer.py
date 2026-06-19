#!/usr/bin/env python3
import sys
from collections import Counter

current_key = None
links_list = []
words_list = []

# Dictionar pentru stocarea frecvențelor globale (toate paginile combinate)
global_words_counter = Counter()


def proceseaza_grup_anterior(key, links, words):
    global global_words_counter
    if not key:
        return

    # Despărțim tipul de cheie și URL-ul
    tip, url = key.split(':', 1)

    if tip == "MAP":
        # S-au colectat toate link-urile unice pentru acest URL
        unice_links = list(set(links))
        print(f"Site-Map pentru {url}:\n\t{str(unice_links)}\n")
    elif tip == "WORD":
        # Calculăm frecvența termenilor pentru această pagină
        counter_pagina = Counter(words)
        # Adăugăm și la contorul global
        global_words_counter.update(counter_pagina)

        # Extragem top 5 cei mai frecvenți termeni din această pagină
        top_5_pagina = counter_pagina.most_common(5)
        print(f"Top 5 termeni in {url}:\n\t{str(top_5_pagina)}\n")


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, val = line.split('\t', 1)

    if current_key == key:
        if key.startswith("MAP:"):
            links_list.append(val)
        else:
            words_list.append(val)
    else:
        proceseaza_grup_anterior(current_key, links_list, words_list)
        current_key = key
        if key.startswith("MAP:"):
            links_list = [val]
            words_list = []
        else:
            links_list = []
            words_list = [val]

# Procesăm ultimul grup citit din flux
proceseaza_grup_anterior(current_key, links_list, words_list)

# Afișăm la final top 5 termeni din TOT setul de pagini
if global_words_counter:
    top_5_global = global_words_counter.most_common(5)
    print(f"TOP 5 TERMENI GLOBALI IN TOT CLUSTERUL:\n\t{str(top_5_global)}")
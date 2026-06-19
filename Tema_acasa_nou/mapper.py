#!/usr/bin/env python3
import sys
import urllib.request
import re
from urllib.parse import urlparse

for line in sys.stdin:
    url = line.strip()
    if not url:
        continue

    try:
        # 1. Facem request HTTP GET pentru a prelua conținutul paginii
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8', errors='ignore')

        # Determină domeniul paginii curente pentru a identifica link-urile interne
        parsed_base = urlparse(url)
        base_domain = parsed_base.netloc

        # 2. Parsare ancore (link-uri)
        links = re.findall(r'href=["\'](https?://[^"\']+|/[^"\']*)["\']', html_content)
        for link in links:
            # Dacă e link relativ (începe cu /), este intern
            if link.startswith('/'):
                link = f"{parsed_base.scheme}://{base_domain}{link}"

            # Verificăm dacă link-ul complet aparține aceluiași domeniu
            if urlparse(link).netloc == base_domain:
                # Trimitem o etichetă specială pentru link-uri: MAP:[url_sursa] -> [link_intern]
                print(f"MAP:{url}\t{link}")

        # 3. Parsare termeni (cuvinte) - curățăm textul simplu de tag-uri HTML
        # Eliminăm scripturile și stilurile
        clean_html = re.sub(r'<(script|style).*?>.*?</\1>', '', html_content, flags=re.DOTALL)
        # Eliminăm restul tag-urilor HTML
        text_only = re.sub(r'<[^>]+>', ' ', clean_html)
        # Extragem cuvintele (doar caractere alfanumerice de lungime >= 3)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text_only.lower())

        for word in words:
            # Trimitem o etichetă specială pentru cuvinte: WORD:[url_sursa] -> [cuvant]
            print(f"WORD:{url}\t{word}")

    except Exception as e:
        # Dacă un URL nu poate fi accesat, îl ignorăm elegant în log-uri ca să nu crape Hadoop
        sys.stderr.write(f"Eroare la accesarea {url}: {str(e)}\n")
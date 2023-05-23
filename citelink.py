#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
name = sys.argv[2]

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

title = soup.find('title')
assert title is not None, "No title found"
title = title.get_text().replace('#', '\\#')

print(f'''@misc{{{name},
    title = {{{{{title}}}}},
    url = {{{url}}},
    note = {{[Accessed 14 May. 2023]}},
}}''')

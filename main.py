#!/bin/python3

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests

import parserList
import firebaseUtils
from datetime import datetime




def print_fiction_list(url):
    html = requests.get(url)
    # html = browser.page_source
    if not html.ok:
        print("request failed\n" + str(html))
    page = BeautifulSoup(html.content, 'html.parser')
    fictions = parserList.parse_list(page)
    print(*fictions, sep="\n")
    # getting time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    firebaseUtils.add_snapshot()

if __name__ == "__main__":
    url = "https://www.royalroad.com/fictions/rising-stars"
    print_fiction_list(url)

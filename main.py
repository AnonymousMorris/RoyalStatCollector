#!/bin/python3

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests

import parserList
from datetime import datetime
import planetScale_utils

def scrape_rising_stars():
    url = "https://www.royalroad.com/fictions/rising-stars"
    fictions = parserList.get_fiction_list(url)

    print(fictions)

    # getting time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


def create_sql_insert(fics, url):
    db = planetScale_utils.pl_db()
    db.push_to_fic(fics)
    db.push_to_rising_stars(fics)


if __name__ == "__main__":
    scrape_rising_stars()

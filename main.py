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
    return fictions
def update_databace(fictions, category):
    db = planetScale_utils.pl_db()
    db.push_to_fic(fictions)
    db.push_to_rating(fics, category)

    # getting time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"scraped and pushed to database at ${current_time}")

if __name__ == "__main__":
    fics = scrape_rising_stars()
    update_databace(fics, "default")
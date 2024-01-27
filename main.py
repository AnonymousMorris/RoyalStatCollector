#!/bin/python3

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests

import parserList
import firebaseUtils
from datetime import datetime





def scrape_push_rising_starts():
    url = "https://www.royalroad.com/fictions/rising-stars"
    fictions = get_fiction_list(url)

    # getting time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    firebaseUtils.add_snapshot(current_time, "rising starts", fictions)


if __name__ == "__main__":
    scrape_push_rising_starts()

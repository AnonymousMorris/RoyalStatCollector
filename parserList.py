
from datetime import datetime, timezone

from bs4 import BeautifulSoup
import re
import requests

from more_itertools import strip


def get_int(str):
    return int(re.compile('\d+').search(str).group())


def parse_fic(fic, crn_time):
    title = fic.find("h2", {"class": "fiction-title"}).text.strip("\n")
    url = fic.find("h2", {"class": "fiction-title"}).find("a")['href']
    id = int(re.search("fiction\/(\d+)", url).group(1))
    stats = fic.find_all("div", {"class": "col-sm-6 uppercase bold font-blue-dark"})
    followers = get_int(stats[0].text.replace(",", ""))
    rating = float(fic.find("div", {"aria-label": re.compile("^Rating:")}).find("span")['title'])
    pages = get_int(stats[2].text.strip("\n"))
    views = get_int(stats[3].text.strip("\n"))
    chapters = get_int(stats[4].text)
    schedule = stats[5].text.strip("\n")
    summary = fic.find("div", {"id": re.compile("^description")}).text
    novel = {
        "title": title,
        "url": url,
        "id": id,
        "followers": followers,
        "rating": rating,
        "pages": pages,
        "views": views,
        "chapters": chapters,
        "schedule": schedule,
        "retrieved_time": crn_time,
        "description": summary,
    }
    return novel


def parse_list(page):
    fictions = page.find("div", {"class": "fiction-list"})
    # print(fictions)
    fiction_items = fictions.find_all("div", {"class": "fiction-list-item row"})
    # print(fiction_items)
    crn_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    fictions = list(map((lambda f: parse_fic(f, crn_time)), fiction_items))
    return fictions


def get_fiction_list(url):
    html = requests.get(url)
    # html = browser.page_source
    if not html.ok:
        print("request failed\n" + str(html))
    page = BeautifulSoup(html.content, 'html.parser')
    fics = parse_list(page)
    # print(*fics, sep="\n")
    return fics

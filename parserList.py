from bs4 import BeautifulSoup
import re

from more_itertools import strip

def get_int(str) :
    return int(re.compile('\d+').search(str).group())


def parse_fic(fic):
    title = fic.find("h2", {"class": "fiction-title"}).text.strip("\n")
    stats = fic.find_all("div", {"class": "col-sm-6 uppercase bold font-blue-dark"})
    followers = get_int(stats[0].text)
    rating = float(fic.find("div", {"aria-label": re.compile("^Rating:")}).find("span")['title'])
    pages = get_int(stats[2].text.strip("\n"))
    views = get_int(stats[3].text.strip("\n"))
    chapters = get_int(stats[4].text)
    schedule = stats[5].text.strip("\n")
    summary = fic.find("div", {"id": re.compile("^description")}).text
    novel = {
        "title": title,
        "followers": followers,
        "rating": rating,
        "pages": pages,
        "views": views,
        "chapters": chapters,
        "schedule": schedule,
        "summary": summary
    }
    return novel


def parse_list(page):
    fictions = page.find("div", {"class": "fiction-list"})
    # print(fictions)
    fiction_items = fictions.find_all("div", {"class": "fiction-list-item row"})
    # print(fiction_items)
    fictions = list(map(parse_fic, fiction_items))
    return fictions

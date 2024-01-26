from bs4 import BeautifulSoup

def parse_list(page):
    fictions = page.find('div', {"class": "fiction-list"})
    print(fictions)
    fiction_items = fictions.find_all("div", {"class": "fiction-list-items"})
    fictions = []
    for fiction in fiction_items:
        title = fiction.find("div", {"class": "fiction-title"})
        stats = fiction.find_all("div", {"class": "col-sm-6 uppercase bold font-blue-dark"})
        followers = stats[0].text
        rating = stats[1].find("span").title
        pages = stats[2].text
        views = stats[3].text
        chapters = stats[4].text
        schedule = stats[5].text
        novel = {
            "title": title,
            "followers": followers,
            "rating": rating,
            "pages": pages,
            "views": views,
            "chapters": chapters,
            "schedule": schedule
        }
        fictions.append(novel)


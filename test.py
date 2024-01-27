import parserList
import requests

import planetScale_utils


def test_push(fics):
    db = planetScale_utils.pl_db()
    db.push_to_fic(fics)


# if __name__ == "__main__":
#     url = "https://www.royalroad.com/fictions/rising-stars"
#     result = parserList.get_fiction_list(url)
#     print(result[0]["url"])
#     test_push(result)

def test_push_to_fic():
    exampleFics = [
        {'title': 'Downtown Druid [Progression Fantasy]', 'url': '/fiction/79173/downtown-druid-progression-fantasy',
         'id': 79173, 'followers': 3, 'rating': 4.83, 'pages': 187, 'views': 202, 'chapters': 31,
         'schedule': 'Jan 27, 2024', 'retrieved_time': '2024-01-27 16:14:16',
         'description': "\nBetrayed by his former gang and thrown into the Rendhold Underprison, Dantes has spent the last five years scraping by. A whoreson of orcish, human, and elvish blood, he's lived on the periphery of the periphery, lying, cheating, and stealing to survive. After a run of bad luck, he's made a powerful enemy. Luckily, he's also gotten all the tools he needs to turn things around.\n\nA slow burn progression fantasy focused on rising through the criminal underworld of a city-state using newfound powers and quick wits.\nMC's powers will develop slowly, but he will use them in creative ways to get ahead, and in the meantime he's not above just braining someone with a club.\nAnti-hero MC with a code.\n1500+ words per chapter\nDaily updates for now, eventually switching to Tues-Thurs-Sat\nThis is my first third-person novel length work, may be some accidental perspective switching, feel free to point it out.\nPatreon is 10 chapters ahead\n"}
    ]
    db = planetScale_utils.pl_db()
    db.push_to_fic(exampleFics)


def test_scrape_then_push():
    url = "https://www.royalroad.com/fictions/rising-stars"
    fictions = parserList.get_fiction_list(url)

    print(*fictions, sep="\n")

    db = planetScale_utils.pl_db()
    db.push_to_fic(fictions)

test_scrape_then_push()
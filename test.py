import parserList
import requests

if __name__ == "__main__":
    url = "https://www.royalroad.com/fictions/rising-stars"
    page = requests.get(url)
    result = parserList.parse_list(page)
    print(result[0]["url"])
import parserList
import requests

if __name__ == "__main__":
    url = "https://www.royalroad.com/fictions/rising-stars"
    result = parserList.get_fiction_list(url)
    print(result[0]["url"])
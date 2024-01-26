# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import selenium
import undetected_chromedriver as uc
from chromedriver_py import binary_path

from bs4 import BeautifulSoup
from selenium import webdriver

import parserList


def print_fiction_list(url):
    svc = webdriver.ChromeService(executable_path=binary_path)
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    browser = uc.Chrome(options=options, service=svc)
    browser.implicitly_wait(10)
    browser.get(url)
    print(browser.title)
    print(browser.page_source + "\n\n")

    browser.quit()
    # html = browser.page_source
    # if html.title:
    #     print("request failed\n" + str(html))
    # page = BeautifulSoup(html, 'html.parser')
    # fictions = parserList.parse_list(page)
    # print(fictions)



if __name__ == "__main__":
    url = "https://www.royalroad.com/fictions/rising-stars"
    print_fiction_list(url)

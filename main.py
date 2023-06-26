import requests
from bs4 import BeautifulSoup

url = "enter your url"
found_links = []

def make_request(url):
    response = requests.get(url)
    data =response.text
    soup = BeautifulSoup(data, 'html.parser')
    return soup


def crawl(url):
    links = make_request(url)
    for link in links.find_all("a"):
        soup_link = link.get('href')
        if soup_link not in found_links:
            found_links.append(soup_link)
            crawl(url)
            print(soup_link)


crawl(url)
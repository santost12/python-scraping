from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}
url = "https://archlinux.org/"

page = requests.get(url, headers=headers)
entire_page = page.text

soup = BeautifulSoup(entire_page, 'html.parser')
news_div = soup.find_all("div", id="news")

for elements in news_div:
    h4_elements = elements.find_all("h4")

    for h4 in h4_elements:
        links = h4.find_all("a",href=True)

        for link in links:
            print(link.get_text())
            print("https://archlinux.org" + link.get("href"))
            print("")

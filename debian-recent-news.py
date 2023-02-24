from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}
url = "https://www.debian.org/News/"

page = requests.get(url, headers=headers)
entire_page = page.text

soup = BeautifulSoup(entire_page, 'html.parser')
news = soup.select('#content > p:nth-child(3)')

for elements in news:
    links = elements.find_all("a",href=True,limit=7)

    for link in links:
        print(link.get_text())
        print("https://www.debian.org/News/" + link.get("href"))
        print("")

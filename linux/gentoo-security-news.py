from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
url = "https://security.gentoo.org/"

page = requests.get(url, headers=headers)
entire_page = page.text

soup = BeautifulSoup(entire_page, 'html.parser')
news_table = soup.find_all("table", {"class": "table table-striped"})

for elements in news_table:
    tr_elements = elements.find_all("tr")

    for th in tr_elements[1:]:
        print(th.get_text())

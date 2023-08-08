from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
url = "https://python.org/blogs/"

page = requests.get(url, headers=headers)
entire_page = page.text

soup = BeautifulSoup(entire_page, 'html.parser')

blog_posts = soup.find_all(class_="list-recent-posts menu")

for element in blog_posts:
    print(element.get_text())

    links = element.find_all("a",href=True)

    for link in links:
        print(link.get('href'))


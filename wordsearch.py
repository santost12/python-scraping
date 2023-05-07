import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
url = "https://en.wikipedia.org/wiki/Bread"

page = requests.get(url, headers=headers)
entire_page = page.text

regex_search = re.findall(r'bread', entire_page, flags=re.IGNORECASE)

counter = 0

for word in regex_search:
    counter += 1

print("[Case insensitive] Found the requested word " + str(counter) + " time(s) on the following URL: " + url)
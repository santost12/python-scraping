import sys
import re
import requests

if len(sys.argv) != 2:
    print("Error: Too many or too few arguments\n")
    print("Example: print-all-urls.py \"https://www.google.com/\"")
    exit()

url = sys.argv[1]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
page = requests.get(url, headers=headers)
entire_page = page.text

https_urls = re.findall(r"\"https://.*?\"", entire_page)
http_urls = re.findall(r"\"http://.*?\"", entire_page)

all_urls = http_urls + https_urls
counter = 0

for url in all_urls:
    print(url)
    counter = counter + 1

print("\nTotal number of URLs found: " + str(counter))

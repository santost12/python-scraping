import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
url = "https://torrentfreak.com/"

page = requests.get(url, headers=headers)
entire_page = page.text

urls = re.findall(r"\"https://torrentfreak\.com/.*?/\"", entire_page)

for url in urls:
    filter = re.search(r"https://torrentfreak.com\/(page|category|wp-json|contact|subscriptions|copyright|privacy|about|#Main).*",url)
    if filter != None:
        pass
    else:
        print(url)

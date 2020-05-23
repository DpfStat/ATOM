import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))
names = []
for i in range(count+1):
    print("retriving: ", url)
    name = re.findall("_([A-Z][a-z].+)\.", url)
    names.append(name)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    urls = list()
    for tag in tags:
# names can be replace with tag.contents[0]
        urls.append(tag.get('href', None))
    url = urls[position-1]
print(names)

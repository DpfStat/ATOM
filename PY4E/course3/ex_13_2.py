import urllib.request, urllib.parse, urllib.error
import json

url = input("enter - ")
data = urllib.request.urlopen(url).read().decode()
print("Retrving: ", url)
print("Retrived: ", len(data))
js = json.loads(data)

sum = 0
for item in js["comments"]:
    print(item)
    count = int(item["count"])
    sum = sum + count
print(sum)

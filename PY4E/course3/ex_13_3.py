import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://py4e-data.dr-chuck.net/json?"
add = input("enter - ")
parm = dict()
parm["address"] = add
parm["key"] = "42"
url = serviceurl+urllib.parse.urlencode(parm)
print("Retriving: ", url)
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
print("retriving: ", len(data), "characters")

try :
    js = json.loads(data)
except :
    js = None

if not js:
    print("===")
    quit()

print(js["results"][0]["place_id"])
for key in js["results"][0].keys():
    print(key)

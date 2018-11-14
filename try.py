import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
sum=0
count=0
data = uh.read()
#print(data.decode())
info = json.loads(data)
info = info["comments"]
#print('User count:', len(info))
for item in info:
    sum=sum+item['count']
    count=count+1
    #print('name', item['name'])
    #print('count', item['count'])
print('count:',count)
print('sum:',sum)

    #print(item)

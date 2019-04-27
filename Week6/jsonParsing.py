from urllib.request import urlopen
import json

url = input("Select url: ")
data = urlopen(url).read()  
info = json.loads(data)
countSum = 0
count = len(info['comments'])

for item in info['comments']:
    commentCount = item['count']
    countSum += commentCount

print(count)
print(countSum)
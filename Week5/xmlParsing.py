from urllib.request import urlopen
import xml.etree.ElementTree as ET

data = input("Select url: ")
xml = urlopen(data).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')

countsSum = 0
for count in counts:
    countsSum += int(count.text)

print(countsSum)

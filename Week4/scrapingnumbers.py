from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen(input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

commentCounts = []

for span in spans:
    commentCounts.append(int(span.string))

print(sum(commentCounts))
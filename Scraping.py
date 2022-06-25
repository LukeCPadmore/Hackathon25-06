import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.youtube.com/watch?v=dJToSyr4yvM')
soup = BeautifulSoup(r.content, 'html.parser')

arrayOfInfo = []

title = soup.find("meta", property = "og:title")["content"]
arrayOfInfo.append(title)

metaContent = soup.find_all("meta", property = "og:video:tag")
for i in metaContent:
    arrayOfInfo.append(i["content"])

for i in range(0,len(arrayOfInfo)):
    print(arrayOfInfo[i])

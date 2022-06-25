import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.youtube.com/watch?v=dJToSyr4yvM')
soup = BeautifulSoup(r.content, 'html.parser')

arrayOfInfo = []

metaContent = [soup.find("meta", property = "og:title")]
metaContent += soup.find_all("meta", property = "og:video:tag")

for i in range(0, len(metaContent)):
    metaContent[i] = metaContent[i]["content"]
    print(metaContent[i])

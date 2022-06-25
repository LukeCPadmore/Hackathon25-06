import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.youtube.com/watch?v=dJToSyr4yvM')
soup = BeautifulSoup(r.content, 'html.parser')
metaContent = soup.find_all("meta",{"property": "og:video:tag"})
for c in metaContent:
    print(c["content"])
#for i in range(0, len(metaContent)):
#    print(metaContent[i])
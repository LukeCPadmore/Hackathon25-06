from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=Q-aiMVY4FkM"

for j in range(0,5):
    driver = webdriver.Chrome(executable_path=r"C:\Users\lucas\%Work\Programs\chromedriver.exe")
    driver.get(url)

    watchLinks = []
    while len(watchLinks) < 3:
        time.sleep(1)

        results = driver.find_elements(
            By.TAG_NAME,
            "a"
        )

        for i in range(0, len(results)):
            try:
                if(results[i].get_attribute("href") != None):
                    if(len(results[i].get_attribute("href").split("watch")) > 1):
                        watchLinks.append(results[i].get_attribute("href"))
            except:
                None

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    arrayOfInfo = []

    metaContent = [soup.find("meta", property="og:title")]
    metaContent += soup.find_all("meta", property="og:video:tag")

    for i in range(0, len(metaContent)):
        metaContent[i] = metaContent[i]["content"]


    print(j , ":", metaContent[0])

    f = open("VideoInfo.txt","a")
    for info in metaContent:
        f.write(info + "\n")
    f.write("--\n")
    f.close()


    url = watchLinks[2]
    driver.close()


        print(j , ":", metaContent[0])

        url = watchLinks[2]


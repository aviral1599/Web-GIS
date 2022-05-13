from bs4 import BeautifulSoup
from lxml import etree
import requests

file1 = open('links1.txt', 'a+', encoding="utf-8")
file2 = open('indiatv_noncrime.txt', 'a+', encoding="utf-8")

link = []

for i in range(1,50):
    try:
        URL = f"https://www.indiatvnews.com/politics/{i}"
        
        webpage = requests.get(URL)
        soup = BeautifulSoup(webpage.content, "html.parser")
        results = soup.find_all('h3',class_='title')
        for j in results:
            p = j.find('a')
            l = p.get('href')
            link.append(l)
            file1.write(l)
            file1.write("\n")
    except:
        pass
    
for u in link:
    try:
        webpage = requests.get(u)
        soup = BeautifulSoup(webpage.content, "html.parser")
        results = soup.find('h1',class_='arttitle')
        #print(results.text)
        file2.write(results.text)
        file2.write("\n")
    except:
        pass
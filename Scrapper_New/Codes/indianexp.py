from bs4 import BeautifulSoup
from lxml import etree
import requests

file1 = open('indianexp_noncrime.txt', 'a+', encoding="utf-8")

l = []

for i in range(1,100):
  URL = f"https://indianexpress.com/page/{i}/?s=entertainment"
      
  webpage = requests.get(URL)
  soup = BeautifulSoup(webpage.content, "html.parser")
  dom = etree.HTML(str(soup))
  res = dom.xpath('//*[@id="section"]/div/div/div[1]/div[3]/div/h3/a/text()')
  for j in res:
    print(j)
    l.append(j)
    file1.write(j)
    file1.write("\n")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)

import time
n=64
lm = int((n-21)/22)
driver.get("https://www.timesnownews.com/mirror-now/crime")
more_buttons = driver.find_element(By.XPATH,'//*[@id="load_more"]/span')
for i in range(lm):
  try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="load_more"]/span')))
    element.click()
    time.sleep(2)
    print("Clicked")
  except:
    break
    
# for x in range(len(more_buttons)):
#   if more_buttons[x].is_displayed():
#       driver.execute_script("arguments[0].click();", more_buttons[x])
#       time.sleep(1)
page_source = driver.page_source

import requests
from bs4 import BeautifulSoup

file = open('timesnow.txt', 'a+', encoding="utf-8")


soup = BeautifulSoup(page_source, "html.parser")
# results = soup.findAll('div', class_="EW1Mb _3v379")
# for r in results:
#   print(r.text)
#   file.write(r.text)
#   file.write("\n")
dom = etree.HTML(str(soup))
res = dom.xpath('//*[@id="app"]/div/div[7]/div[1]/section/div/section/div[1]/div/div[2]/div/a/div/figure/figcaption/div[2]/text()')
for r in res:
  print(r)
  file.write(r)
  file.write("\n")
# driver.quit()
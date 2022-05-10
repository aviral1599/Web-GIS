from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)

import time
n=5000
lm = int((n-20)/10)
driver.get("https://timesofindia.indiatimes.com/topic/crime-india")
more_buttons = driver.find_element(By.XPATH,'//*[@id="storyBody"]/div/div[2]/div/div[1]/div[2]/div[2]/button')
for i in range(lm):
  try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="storyBody"]/div/div[2]/div/div[1]/div[2]/div[2]/button')))
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

file = open('result.txt', 'a+', encoding="utf-8")

URL = "https://timesofindia.indiatimes.com/topic/crime"
page = requests.get(URL)

soup = BeautifulSoup(page_source, "html.parser")
results = soup.findAll('div', class_="EW1Mb _3v379")
for r in results:
  print(r.text)
  file.write(r.text)
  file.write("\n")
# driver.quit()
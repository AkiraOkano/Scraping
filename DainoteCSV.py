'''
Created on 2019/11/28

@author: aokan
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd


html_doc = requests.get("https://review-of-my-life.blogspot.com").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
print(soup.prettify())

real_page_tags = soup.find_all("a")

for tag in real_page_tags:
 print(tag.get("href"))

 tags = soup.find_all("h3", {"class": "post-title"})
for tag in tags:
 print (tag.a.string)
 print (tag.a.get("href"))

 columns = ["name", "url"]
df2 = pd.DataFrame(columns=columns)

# 記事名と記事URLをデータフレームに追加してください
for tag in tags:
 name = tag.a.string
 url = tag.a.get("href")
 se = pd.Series([name, url], columns)
 print(se)
 df2 = df2.append(se, columns)

filename = "result.csv"
df2.to_csv(filename, encoding = 'utf-8-sig') #encoding指定しないと、エラーが起こります。おまじないだともって入力します。

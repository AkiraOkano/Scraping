'''
Created on 2019/12/03

@author: aokan
'''
import pandas as pd
import re
import urllib.request
from re import findall
from pprint import pprint
import requests
from bs4 import BeautifulSoup

import scrapy


url = 'https://info.finance.yahoo.co.jp/ranking/?kd=3&mk=3&tm=d&vl=a'
dfs = pd.read_html(url)
print(dfs[0])

url = "https://www.tripadvisor.jp/Hotels-g298564-Kyoto_Kyoto_Prefecture_Kinki-Hotels.html"
response = urllib.request.urlopen(url)
html1 = response.read()
htmlStr1 = html1.decode()
r1 = re.findall(r'\d,\d+件の口コミ', htmlStr1)
pprint(r1)

r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))


df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
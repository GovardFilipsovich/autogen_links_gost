from bs4 import BeautifulSoup as bs
import requests
import time

links = []

with open('links', 'r') as f:
    links = list(map(lambda x: x.rstrip('\n'), f.readlines()))

for i in links:
    page = requests.get(i)
    soup = bs(page.text, 'html.parser')
    title = soup.find('title').getText()
    print(title, f'- URL: {i} (Дата обращения: {time.strftime("%d.%m.%Y")})')

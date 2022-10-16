import time

from bs4 import BeautifulSoup
import requests
import re
import time

link = "https://www.ebay.com/b/Computer-Printers/1245/bn_320031"
i=1
while True:
    time.sleep(10)
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    a = requests.get(link, headers=headers)
    soup = BeautifulSoup(a.text, 'html.parser')
    # print(soup)
    lists = soup.find_all('div', class_="s-item__info clearfix")
    storage = []
    for index, listsItems in enumerate(lists):
        item_name = listsItems.find('h3').text
        item_price = listsItems.find('span', class_="s-item__price").text
        item1 = (item_name, item_price)
        storage.append(item1)
    print(storage)#item name and price stored as tuples in list 'storage'

    # program to get the link for next page
    # regex
    links=[()]
    k = soup.find_all('a', class_="pagination__item", attrs={'href': re.compile("^https://")})
    m = soup.find_all('a', class_="pagination__item")
    i=i+1
    for kItems in k:
        if kItems.text==i:
            link=kItems.get('href')

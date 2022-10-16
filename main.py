from bs4 import BeautifulSoup
import requests
import re
import time
import sqlite3


conn = sqlite3.connect('storage_data.db')
c=conn.cursor()
#c.execute('''CREATE table items_prices(items TEXT, price FLOAT)''')


link = "https://www.ebay.com/b/Computer-Printers/1245/bn_320031"
i=1
while i<4:
    time.sleep(5)
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    a = requests.get(link, headers=headers)
    soup = BeautifulSoup(a.text, 'html.parser')
    # print(soup)
    lists = soup.find_all('div', class_="s-item__info clearfix")
    storage = []
    for index, All_items_list in enumerate(lists):
        item_name = str(All_items_list.find('h3').text)
        item_price_text = All_items_list.find('span', class_="s-item__price").text
        item_list= list(map(float, re.findall('\d*\.?\d+', item_price_text)))

        price_sum = 0
        divident = 0
        for z in range(len(item_list)):
            price_sum += item_list[z]
            divident = divident + 1
        item_price=price_sum/divident
        print(item_name,"--  $",item_price)
        c.execute('''INSERT INTO items_prices VALUES(?,?)''', (item_name, item_price))
        conn.commit()

    # program to get the link for next page
    # regex
    links=[()]
    k = soup.find_all('a', class_="pagination__item", attrs={'href': re.compile("^https://")})
    m = soup.find_all('a', class_="pagination__item")
    i=i+1
    for kItems in k:
        if kItems.text==i:
            link=kItems.get('href')




from bs4 import BeautifulSoup
import requests
import re
import time
import sqlite3

#sql
conn = sqlite3.connect('storage_data.db')  # connected/created database 'storage_data.db in current directory
cur = conn.cursor()

try :
    cur.execute('''CREATE table items_prices(items TEXT, price FLOAT)''') #table items_prices
except:
    pass

next_page_url = "https://www.ebay.com/b/Computer-Printers/1245/bn_320031" #webpage 1 of listing printer models
counter = 1
while counter < 4:  # the number of webpages to scrape is set to four
    time.sleep(5)

    try:
        #recieves the website data
        headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
        webpage = requests.get(next_page_url, headers=headers)
        soup = BeautifulSoup(webpage.text, 'html.parser')
        # print(soup) #for testing errors
    except:
        print("recheck connection/correct program section which #recieves the website data")
        break

    every_items = soup.find_all('div', class_="s-item__info clearfix")  #scraps every listed items as a whole
    for index, each_item in enumerate(every_items):  # going through each listed items
        item_name = str(each_item.find('h3').text)  # item name
        item_price_text = each_item.find('span', class_="s-item__price").text  # item price scrapped as text as it could be in range of values & is not entirely numbers
        set_of_price_range = list(map(float, re.findall('\d*\.?\d+', item_price_text)))  # regex  to extract the values from text
        # the price is displayed as a range is converted into a set of price range , eg: "anywhere between 8.5 - 9$ => [8.5, 9]
        item_price_add = 0
        divisor = 0
        for each_side_value_position in range(len(set_of_price_range)):  # item_price_range =(#minimum price, #maximum price)
            item_price_add += set_of_price_range[each_side_value_position]
            divisor = divisor + 1
        item_price = item_price_add / divisor  # average price calculated from list of values
        print(item_name, "--  $", item_price)
        cur.execute('''INSERT INTO items_prices VALUES(?,?)''', (item_name, item_price))  # data insertion into table
        conn.commit()

    # program to get the link for next page # regex
    many_urls = soup.find_all('a', class_="pagination__item", attrs={'href': re.compile("^https://")}) #all links with pagenumbers
    counter = counter + 1
    for page_number in many_urls:
        if page_number.text == counter:
            next_page_url = page_number.get('href') #assigned the next-page url

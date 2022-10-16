from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
a=requests.get("https://www.ebay.com/b/Computer-Printers/1245/bn_320031", headers=headers)
soup= BeautifulSoup(a.text,'html.parser')
#print(soup)
lists=soup.find_all('div',class_="s-item__info clearfix")
storage=[]
for index, item in enumerate(lists):
    item_name=item.find('h3').text
    item_price=item.find('span', class_="s-item__price").text
    item1=(item_name, item_price)
    storage.append(item1)
print(storage)

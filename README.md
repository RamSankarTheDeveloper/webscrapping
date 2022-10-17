# webscrapping

  > If you run main.py in your IDE, the program will access [this webpage](https://www.ebay.com/b/Computer-Printers/1245/bn_320031) and scrape each listed items' name and price. This data is edited and stored in 'storage_data.db' on the same directory of your code, in table format. The program will then proceed to sleep for five seconds before accessing the succeeding webpage and the cycle will continue till while loop return false.

**additional libraries you might need to install for it to work -- beautifulsoup4, --regex, -- requests>**


program settings:
  - number of webpages scrapped depends on while loop maxvalue
  - edit 'class_=', intital url if you want to search items other than printers

Languages:
  - python
  - SQL
  - Regex

Libraries used:
  - BeautifulSoup
  - sqlite3
  - requests
  - regex
  - time

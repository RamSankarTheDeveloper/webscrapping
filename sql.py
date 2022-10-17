#file used to reset the table in development phase
import sqlite3

conn = sqlite3.connect('storage_data.db')
c=conn.cursor()
try:
    c.execute('''CREATE table items_prices(items TEXT, price FLOAT)''')  #create table
except:
    pass



#c.execute('''drop table items_prices''')  #delete table

c.execute('''SELECT * from items_prices''')  #display table
print(c.fetchall())  #display table

conn.commit()

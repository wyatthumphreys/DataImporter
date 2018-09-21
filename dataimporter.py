#Wyatt Humnphreys CNA 330 9/20/18

import os, csv, sqlite3

import csv, sqlite3

con = sqlite3.connect("Public_Computer_Access_Locations.db")
cur = con.cursor()
cur.execute("CREATE TABLE t (Lab_name, Phone, Accessible, Hours, Tech_Support, Organization, Location, Web_address);") # use your column names here

with open('Public_Computer_Access_Locations.csv','rb') as fin: # `with` statement available in 2.5+
    #csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Lab_name'], i['Phone'], i['Accessible'], i['Hours'], i['Tech_Support'], i['Organization'], i['Location'], i['Web_address']) for i in dr]

cur.executemany("INSERT INTO t (Lab_name, Phone, Accessible, Hours, Tech_Support, Organization, Location, Web_address) VALUES (?, ?);", to_db)
con.commit()
con.close()

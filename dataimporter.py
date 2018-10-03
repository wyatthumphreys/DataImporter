#Wyatt Humnphreys CNA 330 9/20/18
#Sources: https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
#https://www.periscopedata.com/blog/python-create-table
#https://realpython.com/python-csv/

import os, csv, sqlite3

import csv, sqlite3

con = sqlite3.connect("Public_Computer_Access_Locations.db")
cur = con.cursor()
cur.execute("CREATE TABLE t (Lab_name, Phone, Accessible, Hours, Tech_Support_Assisted, Organization, Location, Web_address);") # use your column names here

with open('Public_Computer_Access_Locations.csv','r') as fin: # Open the spreadsheet and give it the variable name "fin"
    #csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # reads a row from the csv and maps the info to an OrderedDict container. Also preserves order.
    to_db = [(i['Lab_name'], i['Phone'], i['Accessible'], i['Hours'], i['Tech_Support_Assisted'], i['Organization'], i['Location'], i['Web_address']) for i in dr] #Defines to_db as for each entry (i) in dr, make a list with entries in correct order.

cur.executemany("INSERT INTO t (Lab_name, Phone, Accessible, Hours, Tech_Support_Assisted, Organization, Location, Web_address) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db) # Plug in values from the to_db list into the columns of the 't' table based on their order from line 17. The '?' are used for number of items
con.commit()
con.close()

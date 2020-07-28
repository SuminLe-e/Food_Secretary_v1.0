from random import random
from random import randint
import csv
import json
import MySQLdb
from csv import reader

mydb = MySQLdb.connect(host='localhost',
    user=,
    passwd=,
    db=')
cursor = mydb.cursor()

# comment this line if the table is already created
cursor.execute("CREATE TABLE food_list( name VARCHAR(40), quantity INT, unit VARCHAR(20), category VARCHAR(20), storage_type VARCHAR(20), expiry_date DATE, PRIMARY KEY (name, quantity, storage_type, expiry_date));")

with open('foodlist_csvdata.csv', 'r') as csvfile:
    csv_data = reader(csvfile)
    print("here0",csv_data)
    for row in csv_data:
        print(row)
        print("here1")
        print(row[0],row[1],row[2],row[3],row[4],row[5])
        apple = "apple"
        cursor.execute("INSERT INTO food_list (name,quantity,unit,category,storage_type,expiry_date) VALUES (%s,%s,%s,%s,%s,%s)", (row[0],row[1],row[2],row[3],row[4],row[5],))

#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")

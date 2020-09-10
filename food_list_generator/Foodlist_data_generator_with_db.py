from random import random
from random import randint
import csv
import json
import MySQLdb
from csv import reader
import mysql.connector


# mydb = mysql.connector.connect(host='127.0.0.1',
# #     user="root",
# #     passwd="foodsecretary!",
# #     db="food_secretary",
# #     auth_plugin='mysql_native_password')
# # cursor = mydb.cursor()



mydb = MySQLdb.connect(host='localhost',
    user="root",
    passwd="",
    db='mysql_try')
cursor = mydb.cursor()

# comment this line if the table is already created
cursor.execute("CREATE TABLE food_stock_food_list( name VARCHAR(40), quantity INT, unit VARCHAR(20), category VARCHAR(20), storage_type VARCHAR(20), expiry_date DATE, PRIMARY KEY (name, quantity, storage_type, expiry_date));")

with open('foodlist_csvdata.csv', 'r') as csvfile:
    csv_data = reader(csvfile)
    print("here0",csv_data)
    for row in csv_data:
        print(row)
        print("here1")
        print(row[0],row[1],row[2],row[3],row[4],row[5])
        apple = "apple"
        cursor.execute("INSERT INTO food_stock_food_list (name,quantity,unit,category,storage_type,expiry_date) VALUES (%s,%s,%s,%s,%s,%s)", (row[0],row[1],row[2],row[3],row[4],row[5],))

#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")

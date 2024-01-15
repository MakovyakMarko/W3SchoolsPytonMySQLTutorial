# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:48:54 2024

@author: Marko
"""

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'IO8956weqwio',    
    database = 'mydatabase' 
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
sql1 = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql1)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

sql2 = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)

mycursor.execute(sql2, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:39:30 2024

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

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
mycursor.execute("SELECT name,address FROM customers")
myresult = mycursor.fetchall()
print("fetchall:")
for x in myresult:
    print(x)
    

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()
print("fetchone:\n",myresult)
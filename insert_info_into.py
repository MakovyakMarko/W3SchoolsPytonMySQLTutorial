# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:25:41 2024

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

sql = "INSERT INTO customers (name, address) VALUES (%s,%s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record inserted.')

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:14:16 2024

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

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
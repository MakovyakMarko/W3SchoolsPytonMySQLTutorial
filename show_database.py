# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:09:41 2024

@author: Marko
"""


import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'IO8956weqwio'    
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:05:29 2024

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

sql = "DROP TABLE customers"

mycursor.execute(sql)

sql1 = "DROP TABLE IF EXIST customers"

mycursor.execute(sql1)

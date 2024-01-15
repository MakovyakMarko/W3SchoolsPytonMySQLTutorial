# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:16:06 2024

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

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("ALTER TABLE customers ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
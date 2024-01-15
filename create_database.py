# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:06:26 2024

@author: Marko
"""

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= '123456789'    
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
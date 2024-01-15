# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:59:54 2024

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

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

sql1 = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)

mycursor.execute(sql1, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
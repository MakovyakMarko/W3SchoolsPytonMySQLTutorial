# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:14:35 2024

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

#mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
#sql = "INSERT INTO users (name, fav) VALUES (%s,%s)"
#val = [
#    ("John", "154"),
#    ('Peter', '154'),
#    ('Amy', '155'),
#    ('Hannah', ''),
#    ('Michael', '')
#]

#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, 'was inserted.')


#mycursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

#sql1 = "INSERT INTO products (id, name) VALUES (%s,%s)"
#val1 = [
#    ("154", "Chocolate Heaven"),
#    ('155', 'Tasty Lemons'),
#    ('156', 'Vanilla Dreams')
#]

#mycursor.executemany(sql1, val1)

#mydb.commit()

#print(mycursor.rowcount, 'was inserted.')

sql2 = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql2)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    

sql3 = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql3)

myresult = mycursor.fetchall()
print("LEFT JOIN:")
for x in myresult:
    print(x)
    

sql4 = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql4)

myresult = mycursor.fetchall()
print("RIGHT JOIN:")
for x in myresult:
    print(x)
#Create a database by connecting to a existing connection

import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234"
)

mycursor = mydb.cursor()

#mycursor.execute("create database testdb2")
#after creating the database 2 we comment it out
#checking the databases present in the connection

mycursor.execute("show databases")

for x in mycursor:
    print(x)
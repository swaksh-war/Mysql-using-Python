#creating table in a database
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()
mycursor.execute("create table customers (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), address varchar(255))")
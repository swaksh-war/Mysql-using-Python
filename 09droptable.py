import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

# sql = "drop table customers"
# mycursor.execute(sql)

# Drop table if exists

mycursor = mydb.cursor()

sql = "drop table products"

mycursor.execute(sql)
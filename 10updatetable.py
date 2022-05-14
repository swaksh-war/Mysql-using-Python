import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

sql = "update customers set address = 'mumbai' where address= 'bahdurgarh'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()

sql = "update customers set address = %s where address = %s"
val = ("jainpur","lucknow")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "rowcount(s) affected")
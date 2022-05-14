import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()
mycursor.execute("select * from customers limit 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("\n\n\n")
# Selecting from a position

mycursor = mydb.cursor()
mycursor.execute("select * from customers limit 5 offset 2")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
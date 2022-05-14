import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

mycursor.execute("select * from customers order by name")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("\n\n\n\n\n")

mycursor = mydb.cursor()
mycursor.execute("select * from customers order by name desc")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
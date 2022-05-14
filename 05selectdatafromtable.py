#we access table and fetch the data from the table
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

mycursor.execute("select * from products")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("\n\n\n\n\n")

mycursor.execute("select name, address from customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("\n\n\n\n")

mycursor.execute("select name, address from customers")

myresult = mycursor.fetchone()
print(myresult)
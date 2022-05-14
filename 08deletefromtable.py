import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()
# mycursor.execute("delete from customers where address = 'jhajjar'")
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

#Prevent SQL Injection

mycursor = mydb.cursor()
sql = "delete from customers where address = %s"
adr = ('lucknow',)
mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

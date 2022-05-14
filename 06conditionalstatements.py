import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

sql = "select * from customers where name = 'swaksh'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Getting the Wildcard Values

mycursor = mydb.cursor()

sql = "select * from customers where address like '%ata%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#parameterizing for preventing SQL injection

mycursor = mydb.cursor()
sql = "select * from customers where address = %s"
adr = ("kolkata",
)
mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

sql = "select \
    customers.name as user, \
    products.product as favorite \
    from customers \
    inner join products on customers.name = products.name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
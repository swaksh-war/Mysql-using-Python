import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()
sql = "insert into products (name, product) values (%s, %s)"
val = [
    ('swaksh','samsung'),
    ('ashu', 'oppo'),
    ('ankit', 'samsung'),
    ('gaurav', 'samsung'),
    ('sarthak', 'samsung'),
    ('shrayansh', 'samsung'),
    ('krish', 'apple')
]

mycursor.executemany(sql, val)
print(mycursor.lastrowid, "was inserted")
mydb.commit()
print(mycursor.lastrowid, "was inserted")
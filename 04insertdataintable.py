import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swakshwar###1234",
    database = "testdb"
)

mycursor = mydb.cursor()

sql = "insert into customers (name, address) values (%s, %s)"
val = [
   ('swaksh','kolkata'),
   ('ashu','bahdurgarh'),
   ('ankit','jhajjar'),
   ('gaurav','lucknow'),
   ('sarthak', 'delhi'),
   ('shrayansh', 'somewhere in UP'),
   ('Krish', 'jaipur')
]

mycursor.executemany(sql, val)
print(mycursor.lastrowid, "was inserted")   
sql = "insert into customers (name, address) values (%s, %s)"
val =('michelle','blue village')
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.lastrowid, "was inserted")
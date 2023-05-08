import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * from test1.test_table")
for i in mycursor.fetchall():
    print(i)
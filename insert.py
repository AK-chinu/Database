import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(444,'ram',55)")
mydb.commit()
mydb.close()
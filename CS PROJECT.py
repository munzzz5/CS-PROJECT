import mysql.connector
sqlobj = mysql.connector.connect(host="localhost",password="1234",user="root",database="test")
cursor = sqlobj.cursor()
cursor.execute("create table abc (name char(20) , username char(20) , itemwon char(20),rupees_donated int(10)")
con.commit

# Unit 4
# datadbse connection with mysql
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
print(mydb)

# Creating the database
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE mypy')

# printing the list of databases
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)

#Create the table stud in the database mypy
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mypy'
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE stud(ENR INT,NAME VARCHAR(20))')

# inserting the data in the table stud
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mypy'
)
print(mydb)
mysql_insert_query='INSERT INTO stud(ENR,NAME) VALUES(%s,%s)'
records_to_insert=[(1,'abc'),(2,'cde')]
cursor=mydb.cursor()
cursor.executemany(mysql_insert_query,records_to_insert)
mydb.commit()
print(cursor.rowcount,'record insertsscfuly in the table')
cursor.close()
mydb.close()
print('MYSQL connection is closed')

# display records from the table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mypy'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * from stud')
result=mycursor.fetchall()
for i in result:
    print(i)

# Update the record
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mypy'
)
mycursor=mydb.cursor()
updaet_query='UPDATE stud SET ENR=20 WHERE NAME="CDE"'
mycursor.execute(updaet_query)
mydb.commit()

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mypy'
)
mycursor=mydb.cursor()
delete_query='DELETE FROM stud WHERE ENR=20'
mycursor.execute(delete_query)
mydb.commit()
print('record delety suuccessfully ')

#CONNECTION WITH SQLLite

#Coreating the database
import sqlite3
con=sqlite3.connect('data.db')

# # Create atable named stud
con.execute('CREATE TABLE stud (ENR integer,NAME VARCHAR)')

# Insert some records in the table stud
con.execute('''
    INSERT INTO stud VALUES
    (101,'KARTIK'),
    (102,'NIHAL'),
    (103,'HEMANSHU')
    ''')
con.commit()
#Disaplay records
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
    print(i)

#display the stud whose ENR is 103
cursor=con.execute('SELECT * FROM stud WHERE ENR=103')
print(type(cursor))
for i in cursor:
    print(i)   


# update stud whose ENR is 103 to nihal
update='''UPDATE stud SET NAME='NIHALBEN' WHERE ENR=102'''
con.execute(update)
con.commit()
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
    print(i)

#update ENR of the student whose name = HIMANSHU
update='''UPDATE stud SET ENR=100 WHERE NAME="HEMANSHU"'''
con.execute(update)
con.commit()
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
    print(i)

# Delete the student whosw ENR is 102
delete='''DELETE FROM stud WHERE ENR=100'''
con.execute(delete)
con.commit()
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
    print(i)

#Display all records
delete='''DELETE FROM stud '''
con.execute(delete)
con.commit()
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
    print(i)
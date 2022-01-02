#Import your dependencies
import platform
from hdbcli import dbapi
from hdbcli.dbapi import Error

#verify that this is a 64 bit version of Python
print ("Platform architecture: " + platform.architecture()[0])

#Initialize your connection
conn = dbapi.connect(
    address='hana161.lab1.ariba.com',
    port=30015,
    user='paltest',
    password='Paltest123')

#If no errors, print connected
print('connected')

all_commands = ""
cursor = conn.cursor()
with open("../SQL Files/1. arimapipeline.sql", 'r') as file:
    for line in file:
        if line != "":
            try:
                cursor.execute(line)
            except Error:
                print(line, end=": ")
                print(Error)
                continue
    conn.commit()
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print ("%s" % col, end=" ")
    print (" ")
cursor.close()
conn.close()

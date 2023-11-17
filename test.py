from mysql.connector import (connection)

conn   = connection.MySQLConnection (user   = 'gayathri',
                               password = 'Gayathri#1605',
                               host     = 'localhost',
                               database = 'classicmodels', 
                               auth_plugin = 'mysql_native_password',
                               )
cursor = conn.cursor()


# Executing a query
cursor.execute("select * from employees limit 5")


for i in cursor:
    print(i)

cursor.close()
conn.close()
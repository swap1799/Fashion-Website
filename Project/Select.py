import sqlite3


import sqlite3, hashlib, os



conn = sqlite3.connect('database.db')
sql_select_Query = "SELECT * FROM categories"
cursor = conn.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in album is: ", cursor.rowcount)
print("\nPrinting each album record")
for row in records:
    print("email = ", row[1], )
    print("password = ", row[0], "\n")
    #print("password = ", hashlib.md5(row[1].decode()), "\n")
    # print("Price  = ", row[2])
    # print("Purchase date  = ", row[3], "\n")


conn.close()

conn.close()


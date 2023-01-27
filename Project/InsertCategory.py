import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table

conn.execute('''Insert into categories('categoryId','name') values(7,'Other');''')
conn.execute('commit;')

conn.close()


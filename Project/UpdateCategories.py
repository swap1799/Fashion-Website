import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table

conn.execute('''UPDATE categories set name="Other" where name="Accessories";''')
conn.execute('commit;')

conn.close()


import sqlite3


import sqlite3, hashlib, os



conn = sqlite3.connect('database.db')
sql_select_Query = 'Delete from categories where name="Other"'
cursor = conn.cursor()
cursor.execute(sql_select_Query)

sql_ = 'commit'
cursor2 = conn.cursor()
cursor2.execute(sql_)


conn.close()

conn.close()

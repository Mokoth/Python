import sqlite3

connection = sqlite3.connect('hr.db')

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS employees(emp_id INT, name TEXT, position TEXT);""")

connection.commit()
connection.close()

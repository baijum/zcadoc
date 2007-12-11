import os
try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3

curdir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(curdir, 'RData.db')
conn = sqlite3.connect(db_file)

cr = conn.cursor()

cr.execute("""CREATE TABLE members (
                id INTEGER PRIMARY KEY,
                number VARCHAR(15) UNIQUE,
                name VARCHAR(75)
              )""")

cr.execute("""CREATE TABLE books (
                id INTEGER PRIMARY KEY,
                barcode VARCHAR(15) UNIQUE,
                author VARCHAR(75),
                title TEXT
              )""")

cr.execute("""CREATE TABLE circulations (
                id INTEGER PRIMARY KEY,
                member_id INTEGER,
                book_id INTEGER UNIQUE
              )""")

cr.close()
conn.commit()
conn.close()

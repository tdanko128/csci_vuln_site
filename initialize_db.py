import sqlite3
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Database setup
db_path = 'ethreal_realm.db'
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('aeronis', hash_password('Dawnbringers')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('durnik', hash_password('Ironstone')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('finnwise', hash_password('Evergrove')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('kaelen', hash_password('Greenveil')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('lioran', hash_password('Emberstone')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('thalnor', hash_password('Shadowborn')))
    conn.commit()
    conn.close()
    print("Database initialized successfully.")
else:
    print("Database already exists.")

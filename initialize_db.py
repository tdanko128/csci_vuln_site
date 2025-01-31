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
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('frodo', hash_password('ringbearer')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('gandalf', hash_password('you_shall_not_pass')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('aragorn', hash_password('strider')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('legolas', hash_password('greenleaf')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('gimli', hash_password('son_of_gloin')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('sam', hash_password('gardener')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('pippin', hash_password('second_breakfast')))
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('merry', hash_password('brandybuck')))
    conn.commit()
    conn.close()
    print("Database initialized successfully.")
else:
    print("Database already exists.")

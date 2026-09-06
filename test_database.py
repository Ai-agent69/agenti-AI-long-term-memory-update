import sqlite3

db = sqlite3.connect("memory.db")

tables = db.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("Tables:", tables)

db.close()
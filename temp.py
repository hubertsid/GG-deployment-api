import sqlite3

conn = sqlite3.connect("game.db")
c = conn.cursor()
results = c.fetchall()

for res in results[0][3:7]:
    print(res)
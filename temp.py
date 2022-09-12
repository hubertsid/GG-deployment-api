import sqlite3

conn = sqlite3.connect("game.db")
c = conn.cursor()

query = "SELECT * FROM games"
c.execute(query)
results = c.fetchall()
for res in results[0][1:3]:
    print(res)
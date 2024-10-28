import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE News (text TEXT, city TEXT)")
#cursor.execute("CREATE TABLE PrivateAd (text TEXT, expiration_date TEXT)")
#cursor.execute("CREATE TABLE RestaurantReview (text TEXT, rating TEXT)")
text = 'vcj'
rating = 2
cursor.execute("UPDATE News SET publication_date = DATE('now')")

# Вивести список таблиц
tables = cursor.fetchall()
for table in tables:
    print(table[0])
cursor.close()
conn.close()
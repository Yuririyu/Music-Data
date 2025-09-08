import sqlite3

# Connect to new_db.db
conn = sqlite3.connect('new_db.db')
cursor = conn.cursor()

# 1. Total number of musicians and a list of musicians (name and ssn)
cursor.execute("SELECT COUNT(*) FROM Musician")
total_musicians = cursor.fetchone()[0]

cursor.execute("SELECT name, ssn FROM Musician")
musicians = cursor.fetchall()

# 2. Total number of albums and a list of albums recorded at Notown (name and album id)
cursor.execute("SELECT COUNT(*) FROM Album")
total_albums = cursor.fetchone()[0]

cursor.execute("SELECT album_name, album_id FROM Album WHERE album_name LIKE '%Notown%'")
albums = cursor.fetchall()

# 3. Total number of instruments and a list of instruments at Notown (name, key, and id)
cursor.execute("SELECT COUNT(*) FROM Instrument")
total_instruments = cursor.fetchone()[0]

cursor.execute("SELECT instrument_name, key, instrument_id FROM Instrument")
instruments = cursor.fetchall()

# 4. A table of musicians and the total number of albums written by them
cursor.execute("""
SELECT Musician.name, COUNT(Album.album_id) 
FROM Musician
JOIN Album ON Musician.musician_id = Album.musician_id
GROUP BY Musician.musician_id
""")
musician_album_count = cursor.fetchall()

# Print the summary
print(f"1. Total number of musicians: {total_musicians}")
print("List of musicians (name, ssn):")
for musician in musicians:
    print(f"- {musician[0]}, {musician[1]}")

print(f"\n2. Total number of albums: {total_albums}")
print("List of albums recorded at Notown (name, album id):")
for album in albums:
    print(f"- {album[0]}, {album[1]}")

print(f"\n3. Total number of instruments: {total_instruments}")
print("List of instruments at Notown (name, key, id):")
for instrument in instruments:
    print(f"- {instrument[0]}, {instrument[1]}, {instrument[2]}")

print(f"\n4. Musicians and total number of albums written:")
for musician_album in musician_album_count:
    print(f"- {musician_album[0]}: {musician_album[1]} albums")

conn.close()
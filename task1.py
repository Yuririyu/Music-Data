import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('original_db.db')
cursor = conn.cursor()

# Create table to store all fields from the CSV
cursor.execute('''
CREATE TABLE OriginalData (
    num INTEGER,
    street TEXT,
    street_type TEXT,
    name TEXT,
    ssn INTEGER,
    album_id INTEGER,
    album_name TEXT,
    date INTEGER,
    album_type TEXT,
    instrument_id INTEGER,
    instrument_type TEXT,
    key TEXT
)
''')

# Read CSV and insert data
with open('no_town.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        cursor.execute('''
        INSERT INTO OriginalData (num, street, street_type, name, ssn, album_id, album_name, date, album_type, instrument_id, instrument_type, key) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            int(row[0]),   # num
            row[1],        # street
            row[2],        # street_type
            row[3],        # name
            int(row[4]),   # ssn
            int(row[5]),   # album_id
            row[6],        # album_name
            int(row[7]),   # date
            row[8],        # album_type
            int(row[9]),   # instrument_id
            row[10],       # instrument_type
            row[11]        # key
        ))

conn.commit()
conn.close()
import sqlite3

# Connect to a new database
conn = sqlite3.connect('new_db.db')
cursor = conn.cursor()

# Create tables based on the ER-diagram
cursor.execute('''
CREATE TABLE Musician (
    musician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssn INTEGER,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE Album (
    album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    album_type TEXT,
    date INTEGER,
    musician_id INTEGER,
    FOREIGN KEY (musician_id) REFERENCES Musician(musician_id)
)
''')

cursor.execute('''
CREATE TABLE Instrument (
    instrument_id INTEGER PRIMARY KEY,
    instrument_name TEXT,
    instrument_type TEXT,
    key TEXT
)
''')

cursor.execute('''
CREATE TABLE AlbumInstrument (
    album_id INTEGER,
    instrument_id INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album(album_id),
    FOREIGN KEY (instrument_id) REFERENCES Instrument(instrument_id)
)
''')

conn.commit()
conn.close()
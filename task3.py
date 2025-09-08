import sqlite3

# Connect to original_db.db
conn_old = sqlite3.connect('original_db.db')
cursor_old = conn_old.cursor()

# Connect to new_db.db
conn_new = sqlite3.connect('new_db.db')
cursor_new = conn_new.cursor()

# Read all data from the OriginalData table in original_db.db
cursor_old.execute("SELECT * FROM OriginalData")
data = cursor_old.fetchall()

# Insert data into the Musician table
for row in data:
    ssn = row[4]
    name = row[3]
    cursor_new.execute('''
        INSERT INTO Musician (ssn, name) VALUES (?, ?)
    ''', (ssn, name))

# Insert data into the Album table
for row in data:
    album_id = row[5]
    album_name = row[6]
    album_type = row[8]
    date = row[7]
    musician_ssn = row[4]
    
    # Check if the album already exists in the Album table
    cursor_new.execute('''
        SELECT album_id FROM Album WHERE album_id = ?
    ''', (album_id,))
    existing_album = cursor_new.fetchone()
    
    if existing_album is None:  # If the album does not exist, insert it
        cursor_new.execute('''
            INSERT INTO Album (album_id, album_name, album_type, date, musician_id) 
            VALUES (?, ?, ?, ?, (SELECT musician_id FROM Musician WHERE ssn = ?))
        ''', (album_id, album_name, album_type, date, musician_ssn))

# Insert data into the Instrument table
for row in data:
    instrument_id = row[9]
    instrument_name = row[10]
    instrument_type = row[11]
    key = row[11]
    
    # Check if the instrument already exists
    cursor_new.execute('''
        SELECT instrument_id FROM Instrument WHERE instrument_id = ?
    ''', (instrument_id,))
    existing_instrument = cursor_new.fetchone()
    
    if existing_instrument is None:  # If the instrument does not exist, insert it
        cursor_new.execute('''
            INSERT INTO Instrument (instrument_id, instrument_name, instrument_type, key) 
            VALUES (?, ?, ?, ?)
        ''', (instrument_id, instrument_name, instrument_type, key))

# Insert data into the AlbumInstrument table (assumes album_id and instrument_id relationships)
for row in data:
    album_id = row[5]
    instrument_id = row[9]
    cursor_new.execute('''
        INSERT INTO AlbumInstrument (album_id, instrument_id) 
        VALUES (?, ?)
    ''', (album_id, instrument_id))

conn_new.commit()
conn_new.close()
conn_old.close()
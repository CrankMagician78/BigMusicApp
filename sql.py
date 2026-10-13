import sqlite3

#init sql db and setup tables
conn = sqlite3.connect("music.db")
cur = conn.cursor()

#create all tables when imported
cur.execute("""
CREATE TABLE IF NOT EXISTS
Artist (
    Artist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Album_Count INTEGER,
    Song_Count INTEGER,
    Total_Playtime INTEGER
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Album (
    Album_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Song_Count INTEGER,
    Total_Playtime INTEGER
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Song (
    Song_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Album_ID INTEGER REFERENCES Album(Album),
    Song_Length INTEGER,
    Favourited BOOLEAN
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Playlist_Group (
    Group_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Playlist (
    Playlist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Group_ID INTEGER REFERENCES Playlist_Group(Group_ID),
    Song_Count INTEGER,
    Total_Playtime INTEGER
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Artist_Album (
    Artist_ID INTEGER REFERENCES Arist(Artist_ID),
    Album_ID INTEGER REFERENCES Album(Album_ID)
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Artist_Song (
    Artist_ID INTEGER REFERENCES Artist(Arist_ID),
    Song_ID INTEGER REFERENCES Song(Song_ID)
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS
Playlist_Song (
    Playlist_ID INTEGER REFERENCES Playlist(Playlist_ID),
    Song_ID INTEGER REFERENCES Song(Song_ID)
);""")
conn.commit() #commit changes
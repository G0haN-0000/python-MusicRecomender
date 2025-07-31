import sqlite3

# Połączenie z bazą danych (utworzy plik, jeśli nie istnieje)
conn = sqlite3.connect("songs.db")
cursor = conn.cursor()

# Usunięcie starej tabeli, jeśli istnieje
cursor.execute("DROP TABLE IF EXISTS songs")

# Tworzenie nowej tabeli
cursor.execute("""
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    genre TEXT,
    mood TEXT
)
""")

# Lista przykładowych piosenek
songs = [
    ("Blinding Lights", "The Weeknd", "Pop", "Energetic"),
    ("Take On Me", "A-ha", "Pop", "Energetic"),
    ("Someone Like You", "Adele", "Ballad", "Sad"),
    ("Bohemian Rhapsody", "Queen", "Rock", "Epic"),
    ("Shape of You", "Ed Sheeran", "Pop", "Romantic"),
    ("Smells Like Teen Spirit", "Nirvana", "Rock", "Angry"),
    ("Perfect", "Ed Sheeran", "Ballad", "Romantic"),
    ("Believer", "Imagine Dragons", "Rock", "Energetic"),
    ("Lose Yourself", "Eminem", "Hip-Hop", "Motivational"),
    ("Happy", "Pharrell Williams", "Pop", "Happy"),
    ("Rolling in the Deep", "Adele", "Soul", "Powerful"),
    ("Bad Guy", "Billie Eilish", "Pop", "Dark"),
    ("Lovely", "Billie Eilish & Khalid", "Pop", "Sad"),
    ("Radioactive", "Imagine Dragons", "Rock", "Dark"),
    ("Viva La Vida", "Coldplay", "Alternative", "Epic"),
    ("Fix You", "Coldplay", "Alternative", "Emotional"),
    ("Yellow", "Coldplay", "Alternative", "Romantic"),
    ("Hey Jude", "The Beatles", "Rock", "Emotional"),
    ("Let It Be", "The Beatles", "Rock", "Calm"),
    ("All of Me", "John Legend", "Ballad", "Romantic"),
    ("Thinking Out Loud", "Ed Sheeran", "Ballad", "Romantic"),
    ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "Funk", "Energetic"),
    ("Treasure", "Bruno Mars", "Funk", "Happy"),
    ("Grenade", "Bruno Mars", "Pop", "Sad"),
    ("Numb", "Linkin Park", "Rock", "Angsty"),
    ("In the End", "Linkin Park", "Rock", "Dark"),
    ("Humble", "Kendrick Lamar", "Hip-Hop", "Confident"),
    ("God's Plan", "Drake", "Hip-Hop", "Motivational"),
    ("7 Rings", "Ariana Grande", "Pop", "Confident"),
    ("Positions", "Ariana Grande", "Pop", "Romantic"),
    ("Shallow", "Lady Gaga & Bradley Cooper", "Ballad", "Emotional"),
    ("Born This Way", "Lady Gaga", "Pop", "Empowering"),
    ("Bad Romance", "Lady Gaga", "Pop", "Dark"),
    ("Firework", "Katy Perry", "Pop", "Inspirational"),
    ("Dark Horse", "Katy Perry", "Pop", "Mysterious"),
    ("Stronger", "Kanye West", "Hip-Hop", "Energetic"),
    ("We Will Rock You", "Queen", "Rock", "Anthemic"),
    ("We Are the Champions", "Queen", "Rock", "Epic"),
    ("Titanium", "David Guetta ft. Sia", "Electronic", "Powerful"),
    ("Chandelier", "Sia", "Pop", "Emotional"),
    ("Cheap Thrills", "Sia", "Pop", "Dance"),
    ("Wake Me Up", "Avicii", "Electronic", "Motivational"),
    ("Levels", "Avicii", "Electronic", "Energetic"),
    ("Stressed Out", "Twenty One Pilots", "Alternative", "Anxious"),
    ("Ride", "Twenty One Pilots", "Alternative", "Chill"),
    ("Counting Stars", "OneRepublic", "Pop", "Uplifting")
]

# Dodanie danych do tabeli
cursor.executemany("INSERT INTO songs (title, artist, genre, mood) VALUES (?, ?, ?, ?)", songs)

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print(" Baza danych została utworzona i załadowana.")

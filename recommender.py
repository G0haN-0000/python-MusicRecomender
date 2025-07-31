import sqlite3
from difflib import get_close_matches

def find_song(title, cursor):
    cursor.execute("SELECT * FROM songs")
    all_songs = cursor.fetchall()
    titles = [s[1] for s in all_songs]
    matches = get_close_matches(title, titles, n=1, cutoff=0.6)
    if matches:
        cursor.execute("SELECT * FROM songs WHERE title = ?", (matches[0],))
        return cursor.fetchone()
    return None

def recommend(song1, song2, cursor):
    if not song1 or not song2:
        print("Nie znaleziono jednej z piosenek.")
        return

    genre_common = song1[3] if song1[3] == song2[3] else None
    mood_common = song1[4] if song1[4] == song2[4] else None

    query = "SELECT * FROM songs WHERE id NOT IN (?, ?) AND (genre = ? OR mood = ?)"
    cursor.execute(query, (song1[0], song2[0], genre_common, mood_common))
    results = cursor.fetchall()

    if results:
        print("Polecana piosenka podobna do podanych:")
        print(f"{results[0][1]} - {results[0][2]} (Gatunek: {results[0][3]}, Nastrój: {results[0][4]})")
    else:
        print("Nie znaleziono podobnej piosenki.")

def main():
    conn = sqlite3.connect("songs.db")
    cursor = conn.cursor()

    t1 = input("Podaj tytuł pierwszej piosenki: ")
    t2 = input("Podaj tytuł drugiej piosenki: ")

    song1 = find_song(t1, cursor)
    song2 = find_song(t2, cursor)

    recommend(song1, song2, cursor)

    conn.close()

if __name__ == "__main__":
    main()

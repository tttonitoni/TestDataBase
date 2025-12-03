import sqlite3


def abfrage(qurry):
    try:
        sqliteConnection = sqlite3.connect('chinook.db')
        cursor = sqliteConnection.cursor()
        res = cursor.execute(qurry)
        print(res.fetchall())
    except sqlite3.Error as err:
        print(f"SQLite-Fehler: {err}")
    except Exception as err:
        print(f"Unerwarteter Fehler: {err}")
    finally:
        try:
            sqliteConnection.close()
        except Exception:
            pass


abfrage("SELECT tracks.Name, genres.Name FROM tracks LEFT JOIN genres ON tracks.GenreId=genres.GenreId WHERE tracks.GenreId IS NOT NULL;")

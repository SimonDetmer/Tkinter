import sqlite3

def create_connection(db_file):
    """Erstelle eine Datenbankverbindung zu einer SQLite-Datenbank"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Erstelle die Tabelle für das Logbuch"""
    try:
        sql_create_log_table = """CREATE TABLE IF NOT EXISTS log (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    entry TEXT NOT NULL
                                );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_log_table)
    except sqlite3.Error as e:
        print(e)

def insert_entry(conn, entry):
    """Füge einen neuen Eintrag in das Logbuch ein"""
    sql = '''INSERT INTO log(entry) VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, (entry,))
    conn.commit()
    return cur.lastrowid

def fetch_entries(conn):
    """Hole alle Einträge aus dem Logbuch"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM log")
    rows = cur.fetchall()
    return rows

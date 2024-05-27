import sqlite3

# Anbindung an SQLite-Datenbank
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Erstellen der Datenbank
def create_table(conn):
    try:
        sql_create_log_table = """CREATE TABLE IF NOT EXISTS log (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    entry TEXT NOT NULL
                                );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_log_table)
    except sqlite3.Error as e:
        print(e)

# Hinzufügen eines Eintrags
def insert_entry(conn, entry):
    sql = '''INSERT INTO log(entry) VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, (entry,))
    conn.commit()
    return cur.lastrowid

# Laden der vorhandenen Einträge
def fetch_entries(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM log")
    rows = cur.fetchall()
    return rows

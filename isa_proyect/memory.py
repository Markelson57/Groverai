import sqlite3
import threading

class MemoryManager:
    def __init__(self, db_file='memory.db'):
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_tables()
        self.short_term = []  # Memoria RAM para contexto rápido

    def create_tables(self):
        with self.lock:
            cur = self.conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS short_term (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                            entrada TEXT,
                            salida TEXT
                        )''')
            cur.execute('''CREATE TABLE IF NOT EXISTS long_term (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                            entrada TEXT,
                            salida TEXT
                        )''')
            self.conn.commit()

    def add_short_term(self, entrada, salida):
        with self.lock:
            self.short_term.append((entrada, salida))
            if len(self.short_term) > 20:
                self.short_term.pop(0)
            cur = self.conn.cursor()
            cur.execute("INSERT INTO short_term (entrada, salida) VALUES (?, ?)", (entrada, salida))
            self.conn.commit()

    def get_short_term(self, limit=5):
        with self.lock:
            return self.short_term[-limit:]

    def add_long_term(self, entrada, salida):
        with self.lock:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO long_term (entrada, salida) VALUES (?, ?)", (entrada, salida))
            self.conn.commit()

    def get_long_term(self, limit=10):
        with self.lock:
            cur = self.conn.cursor()
            cur.execute("SELECT entrada, salida FROM long_term ORDER BY id DESC LIMIT ?", (limit,))
            return cur.fetchall()

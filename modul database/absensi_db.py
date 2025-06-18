# database/absensi_db.py
import sqlite3
from datetime import datetime

def simpan_absen(nama):
    conn = sqlite3.connect("data_absensi.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS absensi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            waktu TEXT
        )
    ''')
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO absensi (nama, waktu) VALUES (?, ?)", (nama, waktu))
    conn.commit()
    conn.close()
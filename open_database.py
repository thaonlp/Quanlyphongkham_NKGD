import sqlite3

databaseFile = "hsbn.db"

con = sqlite3.connect(databaseFile)

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM DanhSachPhieuKhamBenh')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch(con)
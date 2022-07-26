import sqlite3

databaseFile = "hsbn.db"

con = sqlite3.connect(databaseFile)

def sql_fetch(con):
    cursorObj = con.cursor()
    print("Showing table BenhNhan")
    cursorObj.execute('SELECT * FROM BenhNhan')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    print("Showing table PhieuKhamBenh")
    cursorObj.execute('SELECT * FROM PhieuKhamBenh')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch(con)

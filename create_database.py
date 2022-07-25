import sqlite3

databaseFile = "hsbn.db"

conn = sqlite3.connect(databaseFile)
print("Opened database successfully")

conn.execute('''CREATE TABLE DanhSachPhieuKhamBenh 
       (ID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL, 
       DOB            INT     NOT NULL, 
       ADDRESS        CHAR(100), 
       SEX         CHAR(10),
       JOB CHAR(20),
       PHONE CHAR(20),
       CHECKDAY CHAR(20),
       REASON CHAR(100),
       HISTORY CHAR(100),
       OTHERHIST CHAR(100),
       ALLERGY CHAR(100),
       PLAN TEXT NOT NULL);''')  
print("Table created successfully")
  
conn.close() 

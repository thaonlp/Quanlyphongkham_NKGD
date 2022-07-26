import sqlite3

databaseFile = "hsbn.db"

conn = sqlite3.connect(databaseFile)
print("Opened database successfully")

conn.execute('''CREATE TABLE BenhNhan
       (PATIENTID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL,
       DOB            INT     NOT NULL,
       ADDRESS        CHAR(100), 
       SEX         CHAR(10),
       JOB CHAR(20),
       HISTORY CHAR(100),
       OTHERHIST CHAR(100),
       ALLERGY CHAR(100),
       PHONE CHAR(20));''')

print("Table BenhNhan created successfully")

conn.execute('''CREATE TABLE PhieuKhamBenh
       (ID INT PRIMARY KEY     NOT NULL,
       PATIENTID INT NOT NULL,
       CHECKDAY CHAR(20),
       REASON CHAR(100),
       PLAN TEXT NOT NULL,
       FOREIGN KEY (PATIENTID) REFERENCES BenhNhan (PATIENTID));''')

print("Table PhieuKhamBenh created successfully")
  
conn.close() 

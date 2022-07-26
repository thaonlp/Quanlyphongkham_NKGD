import sqlite3
import openpyxl
from openpyxl import load_workbook
import re

databaseFile = "hsbn.db"
excelFile = "hsbn.xlsx"

def create_fresh_database_table():
       conn = sqlite3.connect(databaseFile)
       print("Opened database successfully")

       """conn.execute('''CREATE TABLE BenhNhan
              (PATIENTID INT PRIMARY KEY     NOT NULL, 
              NAME           TEXT    NOT NULL,
              DOB            INT     NOT NULL,
              ADDRESS        CHAR(100), 
              SEX         CHAR(10),
              NOTE TEXT,
              JOB CHAR(20),
              PHONE CHAR(20));''') """

       # print("Table BenhNhan created successfully")

       conn.execute('''CREATE TABLE PhieuKhamBenh
              (ID INT PRIMARY KEY     NOT NULL,
              PATIENTID INT NOT NULL,
              CHECKDAY CHAR(20),
              REASON CHAR(100),
              PLAN TEXT NOT NULL,
              FOREIGN KEY (PATIENTID) REFERENCES BenhNhan (ID));''')

       print("Table PhieuKhamBenh created successfully")
         
       conn.close() 

create_fresh_database_table()
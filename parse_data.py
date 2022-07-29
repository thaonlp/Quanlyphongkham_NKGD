#!/usr/bin/env python
#
# Convert a set of similarly-structured .xlsx files into a SQLite DB.
#
# For example, say you have hundreds of Excel files in a directory
# called "big-analysis-project" and that each of these Excel files
# has a worksheet containing the same set of columns. Rather than
# having hundreds of separate Excel files, it would be handy to have
# all their data inside one relational database management system.
#
# Pass this script the path to the directory containing said files,
# and this script will create a SQLite database file in the current
# directory.
#
# From there, most operations are a breeze. For instance, looking at
# only the most recent timestamped entry for each user in the dataset:
#
#     SELECT MAX(Last_Updated) AS Latest_Updated, Column_1, Column_2 FROM records GROUP BY Column_2
#

import sys, glob, openpyxl, sqlite3
from sqlalchemy.types import *

databaseFile = "hsbn.db"
excelFile = "hsbn.xlsx"
import pandas as pd

def parse_data():

    db = sqlite3.connect(databaseFile)
    print("Opened database successfully")

    dfs = pd.read_excel(excelFile, sheet_name=None)
    for table, df in dfs.items():
        df.to_sql("BenhNhan", con=db)
    db.commit()
    db.close()

parse_data()

def show_table_column_name():
    dat = sqlite3.connect(databaseFile)
    query = dat.execute("SELECT * From BenhNhan")
    cols = [column[0] for column in query.description]
    print("Table columns ", cols)
    results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    print(results)

def add_more_fields():
    db = sqlite3.connect(databaseFile)
    cursorObj = db.cursor()
    cursorObj.execute("ALTER TABLE BenhNhan ADD SEX CHAR(20);")
    cursorObj.execute("ALTER TABLE BenhNhan ADD JOB CHAR(100);")
    cursorObj.execute("ALTER TABLE BenhNhan ADD PHONE CHAR(30);")
    db.commit()
    db.close()

add_more_fields()
show_table_column_name()
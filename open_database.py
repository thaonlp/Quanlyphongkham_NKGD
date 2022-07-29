import sqlite3
import pandas as pd
databaseFile = "hsbn.db"

def show_table_column_name():
    dat = sqlite3.connect(databaseFile)
    query = dat.execute("SELECT * From BenhNhan")
    cols = [column[0] for column in query.description]
    print("Table columns ", cols)
    #results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    #print(results)


show_table_column_name()

def sql_fetch():
    con = sqlite3.connect(databaseFile)
    cursorObj = con.cursor()
    print("Showing table BenhNhan")
    cursorObj.execute('SELECT * FROM BenhNhan')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    #print("Showing table PhieuKhamBenh")
    #cursorObj.execute('SELECT * FROM PhieuKhamBenh')
    #rows = cursorObj.fetchall()
    #for row in rows:
    #    print(row)
    con.close()

# sql_fetch(con)

def query_name(name, birth):
    query_name = name.upper()
    query_birth = str(birth)
    con = sqlite3.connect(databaseFile)
    query = "SELECT * FROM BenhNhan WHERE FIRSTNAME = '" + query_name + "' AND BIRTH = '" + query_birth + "';"
    print("Query cmd: ", query)
    cursorObj = con.cursor()
    cursorObj.execute(query)
    result = cursorObj.fetchall()
    #df = pd.read_sql(query, con)
    print("Query database when name is ", query_name)
    for x in result:
        print(x)
    con.close()
 
query_name("Thao", 1991) 

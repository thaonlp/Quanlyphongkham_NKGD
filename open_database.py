import sqlite3
import pandas as pd
databaseFile = "hsbn.db"

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

def show_table_column_name():
    dat = sqlite3.connect(databaseFile)
    query1 = dat.execute("SELECT * From BenhNhan")
    colsBN = [column[0] for column in query1.description]
    print("Table columns of BenhNhan", colsBN)
    query2 = dat.execute("SELECT * From PhieuKhamBenh")
    colsPKM = [column[0] for column in query2.description]
    print("Table columns of PhieuKhamBenh", colsPKM)
    # results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    # print(results)
    dat.close()


def query_from_BenhNhan(name, birth):
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
    query1 = con.execute("SELECT * From BenhNhan")
    colsBN = [column[0] for column in query1.description]
    print(colsBN)
    for x in result:
        print(x)
    con.close()
 
# show_table_column_name()
query_from_BenhNhan("Thao", 1991) 

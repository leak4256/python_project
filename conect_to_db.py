import sqlite3



#class connection_db:
#    def __init__(self):
       # pass

def sql_create_table():
    """function to create the db, not for the user"""
    try:
        con = sqlite3.connect('file_last_vs.db')
        con.execute('''CREATE TABLE FILE_NAME
                 (old_name TXT PRIMARY KEY     NOT NULL,
                 new_name           TEXT    NOT NULL);''')
        print ("Table created successfully")
        con.execute("INSERT INTO FILE_NAME VALUES('txt', 'py')")
        con.commit()
    except:
        pass

def sql_update( old, new):
    """update the values in the db"""
    with sqlite3.connect('file_last_vs.db') as con:
        cursorObj = con.cursor()
        cursorObj.execute('UPDATE FILE_NAME SET old_name=(?)', (old,))
        cursorObj.execute('UPDATE FILE_NAME SET new_name=(?)', (new,))
        con.commit()

def sql_select_old_name():
    """select the name that was before the last replace from DB"""
    with sqlite3.connect('file_last_vs.db') as con:
        cursorObj = con.cursor()
        old = cursorObj.execute('SELECT old_name FROM FILE_NAME')
        old = cursorObj.fetchall()[0][0]
    return old

def sql_select_new_name():
    """select for what replaced on the last replace"""
    with sqlite3.connect('file_last_vs.db') as con:
        cursorObj = con.cursor()
        new = cursorObj.execute('SELECT new_name FROM FILE_NAME')
        new = cursorObj.fetchall()[0][0]
    return new

# con = connection_db()
# con.sql_create_table()




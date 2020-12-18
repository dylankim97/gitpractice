import sqlite3
from os import listdir
from os.path import isfile, join


#find . -name "Chrome" 2>/dev/null


con = sqlite3.connect('/Users/dylan/Library/Application Support/Google/Chrome/Default/History')
cursor = con.cursor()
cursor.execute("select url from urls")
result = cursor.fetchall()

for r in result:
    print(r)


con.close()




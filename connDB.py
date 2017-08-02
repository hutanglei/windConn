# -*- coding:utf-8

import cx_Oracle

dsn_tns = cx_Oracle.makedsn('220.248.233.27', 1521, 'zywinddb')

db = cx_Oracle.connect('wind','w1i2n3d4a5',dsn_tns)

cursor = db.cursor()

cursor.execute("select * from SYS.USER_TAB_COLUMNS where TABLE_NAME='AIndexEODPrices' ")

#cursor.execute("select * from user_tab_columns where table_name = 'aindexeodprices'")

row = cursor.fetchall()

for x in row:

    print(x)

cursor.close()
db.close()


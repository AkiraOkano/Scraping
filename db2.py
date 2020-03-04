'''
Created on 2019/11/27

@author: aokan
'''
import ibm_db
import ibm_db_dbi
import pyodbc

#conn = ibm_db_dbi.connect("qcmndb","db2admin","db2admin")
cnx = pyodbc.connect('DSN=QCMNDB; UID=db2admin; PWD=db2admin')
cur = cnx.cursor()

#conn_dbi = ibm_db_dbi.Connection(conn)
#print (conn.tables('db2admin', '%'))
#stmt = ibm_db_dbi.exec_immediate(conn, "UPDATE employee SET bonus = '1000' WHERE job = 'MANAGER'")

#cur = conn.cursor()
sql="select * from SYSCAT.COLUMNS"
cur.execute(sql)

tables = cur.fetchall()
print (tables)
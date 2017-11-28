#!/usr/bin/python

import MySQLdb
bd = MySQLdb.connect(host= 'localhost', port=3306, user = 'root',passwd = 'toor')
cursor = bd.cursor()
cursor.execute("SELECT @@hostname")
data = cursor.fetchone()
print "Nombre del Servidor %s" %data
bd.close()


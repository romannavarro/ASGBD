#!/usr/bin/python

import sys
import os

print "Mostrando argumentos", len(sys.argv)
usuario = sys.argv[1]
clave = sys.argv[2]
baseDatos = sys.argv[3]
cadena = "mysql -u " + usuario + " -p" + clave + " " + baseDatos
print cadena
os.system (cadena)

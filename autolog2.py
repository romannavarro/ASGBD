#!/usr/bin/python


import os
usuario = raw_input("Usuario: ")
clave = raw_input("Password: ")
baseDatos = raw_input("Base de Datos: ")

os.system('mysql --user=' + usuario + ' --password=' + clave + ' --database=' + baseDatos)

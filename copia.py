#!/usr/bin/python
import os
usu =  raw_input ( " Usuario: " )
pas =  raw_input ( " Contraseña: " )
bas =  raw_input ( " Base de Datos: " )

os.system ( ' mysqldump --user = '  + usu +  ' --password = '  + pas +  '  '  + bas +  ' > copia- '  + bas +  ' .sql | tar -cvzf comprimido- '  + bas +  ' - $ (date + % d % m% y-% H% M) .tar ' ' ./copia- '  + bas +  ' .sql ' )


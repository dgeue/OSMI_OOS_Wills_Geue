#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'pcinvent', 'PCinvent12', 'hotel');

    cur = con.cursor()
    cur.execute("SELECT * from buchung")

    ver = cur.fetchone()
    
    print(ver)
    
except mdb.Error:
  
    print("Error %d: %s" )
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:05:11 2020

@author: Robinson Montes
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                           'N%' ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

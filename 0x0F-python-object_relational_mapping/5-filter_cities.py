#!/usr/bin/python3
"""
Created on Sat Aug  8 09:05:11 2020

@author: Robinson Montes
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT cities.name FROM cities WHERE state_id =\
                           (SELECT id FROM states WHERE name LIKE BINARY %s)\
                           ORDER BY cities.id;", (state_name, ))
    rows = cur.fetchall()
    for i, row in enumerate(rows, start=1):
        print(row[0], end='')
        if i < num_rows:
            print(end=', ')
    print()
    cur.close()
    db.close()

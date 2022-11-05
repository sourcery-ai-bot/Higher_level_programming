#!/usr/bin/python3
"""
Created on Sat Aug  8 09:05:11 2020

@author: Robinson Montes
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print(f"Usage: {args[0]} username password database_name")
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{data}'
    )

    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    rows = session.query(City).all()
    for city in rows:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()

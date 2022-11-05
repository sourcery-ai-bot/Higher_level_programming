#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:02:53 2020

@author: Robinson Montes
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = f'https://api.github.com/repos/{username}/{repo}/commits'
    response = get(url)
    try:
        objects = response.json()
        for i, obj in enumerate(objects):
            print(f"{obj.get('sha')}: {obj.get('commit').get('author').get('name')}")
            if i == 9:
                break
    except ValueError:
        pass

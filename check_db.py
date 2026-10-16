"""Tests the connection to your group's database, without Flask.

    python check_db.py

Run this first when something is wrong with the database. It prints ok, or the
real error.
"""

import os

import pymysql
from dotenv import load_dotenv

load_dotenv()

pymysql.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
)
print("ok")

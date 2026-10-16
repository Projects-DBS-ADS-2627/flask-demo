"""Rebuilds the demo tables from ddl.sql, with the test data.

    python database/load_demo_data.py

Uses the same .env as the application. It drops the tables member, gym_class
and booking first, so run it against a demo database only, never against your
group's project database.
"""

import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

load_dotenv()

sql = (Path(__file__).parent / "ddl.sql").read_text(encoding="utf-8")
lines = [line for line in sql.splitlines() if not line.strip().startswith("--")]
statements = [s.strip() for s in "\n".join(lines).split(";") if s.strip()]

connection = pymysql.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
)
with connection:
    with connection.cursor() as cursor:
        for statement in statements:
            cursor.execute(statement)
    connection.commit()

print(f"ok, {len(statements)} statements")

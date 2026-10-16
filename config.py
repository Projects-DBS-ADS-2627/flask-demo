"""Reads the settings from .env, so that no password ends up in the code."""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


def _required(name):
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(
            f"{name} is missing. Copy .env.example to .env in the project root "
            f"and fill in your group's database details from Ufora."
        )
    return value


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")

    # pymysql, not mysqlclient: it installs on every laptop without a compiler
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{quote_plus(_required('DB_USER'))}:{quote_plus(_required('DB_PASSWORD'))}"
        f"@{_required('DB_HOST')}/{_required('DB_NAME')}"
    )

    # 1 in .env prints every query in your terminal
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", "0") == "1"

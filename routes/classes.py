"""The controller for the gym classes.

Step 1: no database yet. The data is a list of dicts with the same fields the
table will have in step 2, so the template does not change when the database
arrives.
"""

from datetime import datetime

from flask import Blueprint, render_template

bp = Blueprint("classes", __name__)

CLASSES = [
    {"id": 1, "name": "Spinning", "starts_at": datetime(2026, 10, 21, 18, 0),
     "capacity": 12, "bookings": ["Lotte", "Ward", "Amira"]},
    {"id": 2, "name": "Yoga", "starts_at": datetime(2026, 10, 22, 7, 30),
     "capacity": 8, "bookings": ["Ward"]},
    {"id": 3, "name": "Boxing", "starts_at": datetime(2026, 10, 23, 19, 0),
     "capacity": 10, "bookings": []},
]


@bp.route("/classes")
def class_list():
    return render_template("classes.html", classes=CLASSES)

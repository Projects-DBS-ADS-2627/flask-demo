"""The controller for the general pages.

Make one file per part of your application (routes/listings.py,
routes/bookings.py, ...), each with its own Blueprint, and register it in app.py.

In a routes file you write @bp.route instead of @app.route. The only other
difference: in url_for you add the file's name, url_for("main.home").
"""

from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")

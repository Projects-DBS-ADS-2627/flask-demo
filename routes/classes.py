"""The controller for the gym classes.

Step 2: the data comes from the database. The template did not change.
"""

from flask import Blueprint, render_template

from models import GymClass

bp = Blueprint("classes", __name__)


@bp.route("/classes")
def class_list():
    classes = GymClass.query.order_by(GymClass.starts_at).all()
    return render_template("classes.html", classes=classes)


@bp.route("/classes/<int:class_id>")
def class_detail(class_id):
    gym_class = GymClass.query.get_or_404(class_id)
    return render_template("class.html", gym_class=gym_class)

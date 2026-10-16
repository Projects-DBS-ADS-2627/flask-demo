"""The controller for the gym classes.

Step 3: a form that changes the database. Every write follows the same three
steps: check, write, redirect.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

from models import Booking, GymClass, Member, db

bp = Blueprint("classes", __name__)


@bp.route("/classes")
def class_list():
    classes = GymClass.query.order_by(GymClass.starts_at).all()
    return render_template("classes.html", classes=classes)


@bp.route("/classes/<int:class_id>")
def class_detail(class_id):
    gym_class = GymClass.query.get_or_404(class_id)
    members = Member.query.order_by(Member.name).all()
    return render_template("class.html", gym_class=gym_class, members=members)


@bp.route("/classes/<int:class_id>/book", methods=["POST"])
def book(class_id):
    gym_class = GymClass.query.get_or_404(class_id)
    member_id = int(request.form["member_id"])

    # The route decides whether it is allowed. Not the template, not the user.
    if len(gym_class.bookings) >= gym_class.capacity:
        flash("That class is full.")
        return redirect(url_for("classes.class_detail", class_id=class_id))

    try:
        db.session.add(Booking(member_id=member_id, class_id=class_id))
        db.session.commit()
        flash("Booked.")
    except IntegrityError:
        # UNIQUE (member_id, class_id) in the DDL: this member already has a spot
        db.session.rollback()
        flash("That member is already booked for this class.")

    # Never render_template after a POST: refresh would book twice
    return redirect(url_for("classes.class_detail", class_id=class_id))

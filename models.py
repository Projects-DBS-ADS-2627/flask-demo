"""The model: one class per table in your DDL.

Every column here is a column in database/ddl.sql, with the same name and type.
The DDL is the truth: change the table first, then the class, and tell your group.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    __tablename__ = "member"
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class GymClass(db.Model):
    __tablename__ = "gym_class"
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(80), nullable=False)
    starts_at = db.Column(db.DateTime, nullable=False)
    capacity  = db.Column(db.Integer, nullable=False)

    # Not a column: lets you write gym_class.bookings instead of a second query
    bookings = db.relationship("Booking", backref="gym_class")


class Booking(db.Model):
    __tablename__ = "booking"
    id        = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    class_id  = db.Column(db.Integer, db.ForeignKey("gym_class.id"), nullable=False)

    member = db.relationship("Member")

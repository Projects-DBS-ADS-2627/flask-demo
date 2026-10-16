"""The model: one class per table in your DDL.

Every column here is a column in database/ddl.sql, with the same name and type.
The DDL is the truth: change the table first, then the class, and tell your group.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# An example of what a class looks like. Replace it with your own tables.
#
# class Listing(db.Model):
#     __tablename__ = "listing"
#     id          = db.Column(db.Integer, primary_key=True)
#     title       = db.Column(db.String(120), nullable=False)
#     price       = db.Column(db.Numeric(8, 2), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

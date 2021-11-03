"""Item DB Model"""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):  # pylint: disable=too-few-public-methods
    """Item model class"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, default=0)
    thumbnail = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(200), nullable=False)


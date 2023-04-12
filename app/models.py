# Add any model classes for Flask-SQLAlchemy here
from . import db


class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    poster = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at
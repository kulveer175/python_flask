from .db import db

#Data Model for Books
class Books(db.Document):
    _id = db.IntField()
    author = db.StringField(required=True)
    country = db.StringField(required=True)
    imageLink = db.StringField(required=True)
    language = db.StringField(required=True)
    link = db.StringField(required=True)
    pages = db.IntField(required=True)
    title = db.StringField(required=True)
    year = db.IntField(required=True)

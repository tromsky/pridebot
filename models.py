import datetime

from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
    TextField,
)

db = SqliteDatabase("db.sqlite3")


class BaseModel(Model):
    """
    Base
    """

    class Meta:
        """
        Database
        """

        database = db


class User(BaseModel):
    """
    Twitter users
    """

    username = CharField(unique=True)
    created_date = DateTimeField(default=datetime.datetime.now)


class ProfilePicture(BaseModel):
    """
    Twitter user profile pictures
    """

    user = ForeignKeyField(User, backref="profile_pictures")
    url = TextField()
    local_path = TextField()
    has_rainbow = BooleanField()
    created_date = DateTimeField(default=datetime.datetime.now)

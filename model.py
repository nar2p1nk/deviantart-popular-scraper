from peewee import *

db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    userId = AutoField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()
    profilePicture = CharField()

class Post(BaseModel):
    postId = AutoField(primary_key=True)
    displayImageLink = CharField()
    originalImageLink = CharField()
    numFavourites = IntegerField(default=0)
    numViews = IntegerField(default=0)
    numComments =  IntegerField(default=0)
    PostedBy = ForeignKeyField(User, backref='posts')
    timePosted = DateTimeField()


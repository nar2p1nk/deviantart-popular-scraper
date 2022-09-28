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
#    displayImageLink = CharField()
#    originalImageLink = CharField()
    numFavourites = IntegerField(default=0)
    numViews = IntegerField(default=0)
    numComments =  IntegerField(default=0)
    PostedBy = ForeignKeyField(User, backref='posts')
    timePosted = DateTimeField()


class OtherUser(BaseModel):
    otherId = AutoField(primary_key=True)
    username = CharField(unique=True)
    profilePictureLink = CharField()
    userProfileLink = CharField()
    postLink = CharField()

class OtherPost(BaseModel):
    postId = AutoField(primary_key=True)
    displayImageLink = CharField()
    originalImageLink = CharField()
    numFavourites = IntegerField(default=0)
    numViews = IntegerField(default=0)
    numComments =  IntegerField(default=0)
    PostedBy = ForeignKeyField(OtherUser, backref='posts')
    timePosted = DateTimeField()


db.connect()

db.create_tables([User,Post,OtherUser,OtherPost])

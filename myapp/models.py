from django.db.models import *

# Create your models here.


class User(Model):
    id = CharField(max_length=256, primary_key=True)
    pw = CharField(max_length=256)


class Movie(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Start(Model):
    id = AutoField(primary_key=True)
    stargazer = OneToOneField(User, on_delete=CASCADE)
    movie = OneToOneField(Movie, on_delete=CASCADE)

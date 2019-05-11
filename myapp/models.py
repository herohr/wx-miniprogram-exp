import json

from django.db.models import *


# Create your models here.


class User(Model):
    id = CharField(max_length=256, primary_key=True)
    pw = CharField(max_length=256)


class Movie(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    actor = CharField(max_length=128)

    star = PositiveIntegerField(default=0)

    @staticmethod
    def serialize(query_set, this_name=None):
        data = [{"id": i.id, "name": i.name, "actor": i.actor, "star": i.star} for i in query_set]
        if this_name is not None:
            data = {this_name: data}
        return json.dumps(data)


# class Star(Model):
#     id = AutoField(primary_key=True)
#     num = PositiveIntegerField(default=0)
#     # stargazer = OneToOneField(User, on_delete=CASCADE)
#     movie = ForeignKey(Movie, on_delete=CASCADE)
#
#     @staticmethod
#     def serialize(query_set, this_name=None):
#         data = [{"id": i.id, "num": i.num, "movie_id": i.movie.id} for i in query_set]
#         if this_name is not None:
#             data = {this_name: data}
#         return json.dumps(data)


def movie_init():
    m1 = Movie(name="大侦探皮卡丘 Pokémon Detective Pikachu", actor="罗伯·莱特曼")
    m2 = Movie(name="复仇者联盟4：终局之战 Avengers: Endgame", actor="安东尼·罗素 / 乔·罗素")
    m3 = Movie(name="一个母亲的复仇 Mom", actor="拉维·德耶瓦尔")
    m4 = Movie(name="何以为家 كفرناحوم", actor=" 娜丁·拉巴基")
    m5 = Movie(name="下一任：前任", actor="陈鸿仪")
    m1.save()
    m2.save()
    m3.save()
    m4.save()
    m5.save()

#
# movie_init()

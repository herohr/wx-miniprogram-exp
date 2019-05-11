import json

from django.shortcuts import render
from django.views.generic import View, TemplateView
from myapp.models import User, Movie
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize


# Create your views here.


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        data = Movie.serialize(movies, "movies")
        print(data)
        return HttpResponse(data)


class MovieStar(View):
    # def get(self, request):
    #     movie_id = request.GET["movie_id"]
    #     movie = Movie.objects.get(id=movie_id)
    #
    #     movie_star = Star.objects.get(movie=movie)
    #     data = serialize("json", movie_star)
    #
    #     return data

    def post(self, request):
        movie_id = request.POST["movie_id"]
        movie = Movie.objects.get(id=movie_id)
        movie.star += 1
        movie.save()
        return HttpResponse(json.dumps({"star": movie.star}))


class MovieTemplateView(TemplateView):
    template_name = "movie.html"

from django.shortcuts import render
from django.views.generic import View
from myapp.models import User
from django.http import HttpResponse
# Create your views here.


class MovieView(View):
    movie_star = 0

    def post(self, request):
        self.movie_star += 1
        return HttpResponse("success")

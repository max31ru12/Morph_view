from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def doctor_view(request):
    return HttpResponse('<h1>Это страница дл врачей</h1>')

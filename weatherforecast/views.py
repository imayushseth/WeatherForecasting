from django.http import HttpResponse
from django.shortcuts import render


# /weatherforecast -> index

def index(request):
    return render(request, 'index.html')


# /ar -> ar

def ar(request):
    return HttpResponse('AR here')


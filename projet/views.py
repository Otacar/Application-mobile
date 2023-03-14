from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def list_secher(request):
    return HttpResponse('Liste des machines à sécher')

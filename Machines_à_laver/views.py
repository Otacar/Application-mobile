from django.shortcuts import render
from django.http import  HttpResponse

def list_laver(request):
    return render(request, 'Machines_à_laver/machines_laver.html')

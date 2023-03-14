from django.shortcuts import render


def list_secher(request):
    return render(request , 'Machines_à_sécher/machines_secher.html')

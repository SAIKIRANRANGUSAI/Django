from django.shortcuts import render
from .models import Data

def sai(request):
    data = Data.objects.all()
    return render(request, 'main.html', {'data': data})

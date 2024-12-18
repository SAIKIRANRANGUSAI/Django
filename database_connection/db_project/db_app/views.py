from django.shortcuts import render
from .models import Data
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def sai(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        s = Data(name=name, age=age, address=address)
        s.save()
        return HttpResponse("<h2>Record Added Successfully</h2>")
        
    return render(request, 'p_ost.html')

@csrf_exempt
def get_update(request, id):
    hm = Data.objects.get(id=id)
    hm.name = "rangusaikiran"
    hm.save()
    return HttpResponse("data updateded sucessfully")

@csrf_exempt
def update_s(request, id):
    h = Data.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        h.name = name
        h.age = age
        h.address = address
        h.save()
        return HttpResponse("<h2>Record updated Successfully</h2>")
    h = Data.objects.get(id=id)
    return render(request, 'update_get.html', {'h': h})
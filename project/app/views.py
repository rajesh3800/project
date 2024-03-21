from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            TO = Todo(name=title,desc=desc)
            TO.save()
    elif request.method == 'GET':
        sno = request.GET.get('sno')
        Todo.objects.filter(sno=sno).delete()
        alltodos = Todo.objects.all()
        d = {'alltodos':alltodos}
    return render(request, 'home.html',d)
sno = 0
def update(request):
    if request.method == 'GET':
        global sno
        sno = request.GET.get('sno')
        return render(request, 'update.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        Todo.objects.filter(sno=sno).update(name=title,desc=desc)
        alltodos = Todo.objects.all()
        d = {'alltodos':alltodos}
        return render(request, 'home.html',d)
    return render(request, 'update.html')
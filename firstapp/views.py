from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def add(request):
    val=request.POST.get('a')
    val2=request.POST.get('b')
    s=int(val)+int(val2)

    return render(request,"add.html",context={'sum':s})

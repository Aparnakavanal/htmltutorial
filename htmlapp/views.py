from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home.html")

def pone(request):
    return render(request,"pageone.html")

def ptwo(request):
    return render(request,"pagetwo.html")

def pthree(request):
    return render(request,"pagethree.html")

def pfour(request):
    return render(request,"pagefour.html")

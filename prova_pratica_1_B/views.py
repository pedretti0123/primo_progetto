from django.shortcuts import render
import random

def massimo(request):
    var1 = random.randint(1,20)
    var2 = random.randint(1,20)
    var3 = random.randint(1,20)
    return render(request, "massimo.html", {'var1': var1, 'var2': var2, 'var3': var3})

def pari(request):
    list1=[]
    for i in range(30):
        list1.append(random.randint(1,20))
    return render(request, "pari.html", {'list1': list1})

def index(request):
    return render(request, "index.html")

def studenti(request):
    return render(request, "studenti.html")


from django.shortcuts import render

def es_if(request):
    return render(request, "seconda_app/es_if.html")

def if_else_elif(request):
    return render(request, "seconda_app/if_else_elif.html")

def index(request):
    return render(request, "seconda_app/index.html")



    
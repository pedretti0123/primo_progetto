from django.shortcuts import render
import datetime

def es_if(request):
    return render(request, "seconda_app/es_if.html")

def if_else_elif(request):
    return render(request, "seconda_app/if_else_elif.html")

def index(request):
    return render(request, "seconda_app/index.html")

def esempio_for(request):
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "seconda_app/es_for.html", dic)

def esempio_for(request):
    dic = { 
        'list1': [1, datetime.date(2019, 7, 16), 'Do not give up!'],
        'list2': [1, datetime.date(2019, 7, 16), 'Do not give up!'],
        'my_dict': {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}
    }
    return render(request, "seconda_app/es_for.html", dic)

    
'''from django.http import HttpResponse
from .models import Articolo,Giornalista
def home(request):
        a=""
        g=""
        for art in Articolo.objects.all():
            a+=art.titolo+"<br>"

        for gio in Giornalista.objects.all():
            g+=(gio.nome+a+"<br> Giornalisti:<br>"+g)

        return HttpResponse("<h1>"+ response+"</h1")    
'''
from django.shortcuts import render
from .models import Articolo, Giornalista

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {
        'articoli': articoli,
        'giornalisti': giornalisti
    }
    return render(request, 'homepage.html', context)
    
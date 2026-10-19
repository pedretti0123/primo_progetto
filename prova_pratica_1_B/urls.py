from django.urls import path

from .views import massimo, pari, index,studenti

app_name="prova_pratica_1_B"

urlpatterns = [
    path('', index, name='index'),
	path("massimo", massimo, name="massimo"),
	path("pari", pari, name="pari"),
	path("studenti", studenti, name="studenti"),
]

from django.urls import path
from .views import home, articoloDetailView,lista_articoli,queryBase

app_name = "news"  

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>/", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>/", lista_articoli, name="lista_articoli"),
    path("lista_articoli/", lista_articoli, name="lista_articoli"),
    path("query/", queryBase, name="query_base"),
]
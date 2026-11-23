from django.urls import path
from .views import home, articoloDetailView, lista_articoli, queryBase, giornalistaDetailView, index_news, lista_giornalisti

app_name = "news"  

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>/", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>/", lista_articoli, name="lista_articoli"),
    path("lista_articoli/", lista_articoli, name="lista_articoli"),
    path("query/", queryBase, name="query_base"),
    path("giornalisti/<int:pk>/", giornalistaDetailView, name="giornalistaDetailView"),
    path("index_news/", index_news, name="index_news"),
    path("lista_giornalisti/", lista_giornalisti, name="lista_giornalisti"),
]
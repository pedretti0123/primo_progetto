from django.contrib import admin
from django.urls import path, include
from primo_progetto.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/', include("prima_app.urls",namespace="prima_app")),
    path('', index, name="index"),
    path('seconda_app/', include("seconda_app.urls",namespace="seconda_app")),
    path('prova_pratica_1_B/', include("prova_pratica_1_B.urls",namespace="primo_progetto_1_B")),


]
from django.urls import path

from .views import es_if, if_else_elif, index,esempio_for

app_name="seconda_app"

urlpatterns = [
	path("es_if", es_if, name="es_if"),
	path('', index, name='index'),
	path("if_else_elif", if_else_elif, name="if_else_elif"),
	path("es_for", esempio_for, name="es_for"),
]

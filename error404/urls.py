from django.urls import path
from . import views

app_name= 'error404'


urlpatterns = [
    path('', views.index, name='index'),
]
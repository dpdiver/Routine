from django.urls import path

from . import views

app_name = 'routine'

urlpatterns = [
    path('', views.index, name='index'),
]
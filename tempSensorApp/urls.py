from django.urls import path
from .views import data, home

urlpatterns = [
    path('api/data', data, name="data"),
    path('', home, name="home"),
]

from json.tool import main
from unicodedata import name
from django.urls import path,include
from demoapp import views

urlpatterns = [
    path('index/',views.index,name='home'),
]
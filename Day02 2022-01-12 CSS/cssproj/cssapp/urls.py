
from django.urls import path
from cssapp import views
urlpatterns = [
    path('index/', views.index,name='home'),
]

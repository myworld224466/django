from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    context={'title':'home'}
    return render(request,'demoapp/index.html',context)

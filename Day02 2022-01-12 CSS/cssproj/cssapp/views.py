from django.shortcuts import render

# Create your views here.
def index(request):
    context={}  #This is a dictionary
    return render(request,'index.html',context)

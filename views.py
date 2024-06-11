from django.shortcuts import render # type: ignore
from .models import *

# Create your views here.
def home(request):
    req= Professeurs.objects.all()
    return render(request,'index.html',{'req':req})

def services(request):
    req= Services.objects.all()
    return render(request,'services.html',{'req':req})

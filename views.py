from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from.models import Formalshirt,Tshirt,Shirts

# Create your views here.

def home(request): 
    #flist=Formalshirt.objects.all()
    flist=get_list_or_404(Formalshirt)
    return render(request, 'home.html', {'flist':flist})

def details(request, fstr):
    fobj= Formalshirt.objects.get(name=fstr)
    return render(request,'details.html',{'f':fobj})

def tshirt(request):
    tlist = get_list_or_404(Tshirt)
    return render(request, 'Tshirt.html', {'tlist': tlist})
def tdetails(request, tstr):
    tobj= Tshirt.objects.get(name=tstr)
    return render(request,'tdetails.html',{'t':tobj})

def shirts(request):
    slist = get_list_or_404(Shirts)
    return render(request, 'shirts.html', {'slist': slist})
def sdetails(request, sstr):
    sobj= Shirts.objects.get(name=sstr)
    return render(request,'sdetails.html',{'s':sobj})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')






from django.shortcuts import render
from testApp.models import *

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hydjobs(request):
    jobs_list=Hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/hyd.html',context=my_dict)

def pune(request):
    jobs_list=Pune.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/pune.html',context=my_dict)

def chennai(request):
    jobs_list=Chennai.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/chennai.html', context=my_dict)

def bang(request):
    jobs_list = Bang.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/bang.html', context=my_dict)


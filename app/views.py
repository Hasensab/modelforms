from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        FO=TopicForm(request.POST)
        if FO.is_valid():
            FO.save()
            return HttpResponse('insertion of data done')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insertion of data done')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EARFO=AccessForm()
    d={'EARFO':EARFO}
    if request.method=='POST':
        A=AccessForm(request.POST)
        if A.is_valid():
            A.save()
            return HttpResponse('insertion of data done')
    return render(request,'insert_accessrecord.html',d)
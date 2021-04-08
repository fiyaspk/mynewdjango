from django.shortcuts import render
from django.http import HttpResponse
def testfn(request):
    return HttpResponse('heloooo')
def html(request):
    return render(request,'cricket league.html')        


# Create your views here.

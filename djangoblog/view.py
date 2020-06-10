from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    # return httpsesponse("hi there")
    return render(request,'about.html')
def home(request):
    # return httpsesponse('Home')
    return render(request,'Home.html')

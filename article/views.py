from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def article_list(request):
    article=models.Article.objects.all().order_by('date')
    args = {'article':article} 
    return render(request,'article/art_list.html',args) 
def article_detail(request,slug):
    # return HttpResponse(slug)
    article=models.Article.objects.get(slug=slug)
    return render(request,'article/articl_detail.html',{'article':article})


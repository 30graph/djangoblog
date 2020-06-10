from django.contrib import admin
from django.urls import path ,include
from . import view
from  django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',view.about),
    path('',view.home),
    path('article/',include('article.urls'))
]

urlpatterns += staticfiles_urlpatterns()
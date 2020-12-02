from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   # path('app3/', include('app3.urls')),
    path('', views.index, name='index'),
]
    
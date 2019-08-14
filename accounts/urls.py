from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.ecSeg.as_view(), name='ecSeg'),
    path('home/', views.home.as_view(), name='home'),

]

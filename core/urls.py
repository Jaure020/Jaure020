from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Sign_up.as_view(), name='signup'),
    path('', views.Photo_form.as_view(), name='ecSeg'),
    path('home/', views.home.as_view(), name='home'),

]

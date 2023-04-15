from django.contrib import admin
from django.urls import path,include
from grid import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('register',views.register,name='register'),
    path('nearby',views.nearby,name='nearby')   
    
]
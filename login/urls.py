from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('loginlist/',views.loginlist,name='loginlist'),
    path('loginadd/',views.add,name='add'),
    path('login/',views.Login,name='login'),
]
from django.urls import path
from . import views

urlpatterns =[
    path('', views.login),
    path('codepage/', views.codepage),
    path('submit/', views.finish),
    path('sign/', views.sign),
    path('last/', views.last),
]
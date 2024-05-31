from django.urls import path
from . import views

urlpatterns =[
    path('index/', views.index, name='index'),
    path('home/',views.home,name='home'),
  #  path('day_time/',views.day_time,name='day_time'),
  #  path('message/',views.message,name='message')
]
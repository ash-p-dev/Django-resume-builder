from django.urls import path
from . import views

urlpatterns = [
    path('template2/', views.template2, name='template2'),
    path('about/', views.about, name='about'),
    path('resume/', views.home, name="home"),
    path('',views.info,name="info")
]

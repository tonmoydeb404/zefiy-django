from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="website.home"),
    path('about/', views.about, name="website.about"),
    path('services/', views.services, name="website.services")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check-in/', views.check_in, name='check_in'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home" ),
    path('<str:city>/', views.home, name='home'),
]

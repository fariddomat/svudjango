from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("store", views.store, name="store"),
    path("reset", views.reset, name="reset"),
    path("v1/", views.v1, name="view1"),
    
]

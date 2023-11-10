from django.urls import path
from vote_app import views

urlpatterns = [
    path("", views.home, name="home"),
]
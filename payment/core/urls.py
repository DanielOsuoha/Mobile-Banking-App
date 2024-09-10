from . import views
from django.urls import path

url_patterns = [
    path("", views.home, name="home")
]
from django.urls import path
from . import views

app_name = "core"  


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('contact/', views.home, name='contact')
]
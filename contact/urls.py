from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
import contact

urlpatterns = [
     path('contact/', views.index, name='index'),
]

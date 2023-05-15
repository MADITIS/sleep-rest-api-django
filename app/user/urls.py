from django.urls import path
from .views import register

urlpatterns = [
    path('create/', register, name='register'),
]

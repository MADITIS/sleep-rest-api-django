from django.urls import path
from .views import register, home

urlpatterns = [
    path('create/', register, name='register'),
    path('<int:userId>/improvement/', home, name='not implemented')
]path

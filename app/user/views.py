from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .models import Improvement

from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import RegisterForm


def home(request):
    form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('sleep_improvements')


def sleep_improvements(request):
    improvements = Improvement.objects.all()
    return render(request, 'user/sleep_improvements.html', {'improvements': improvements})

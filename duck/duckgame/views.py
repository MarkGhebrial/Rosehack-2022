from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.
def index(request):
    return render(request, "index.html")

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(index)
    else:
        pass

def update_leaderboard(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseForbidden('Not authorized')

    # request.user

    return HttpResponse('Testing, testing, 1, 2, 3')
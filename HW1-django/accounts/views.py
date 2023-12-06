from django.shortcuts import render
from .models import UserProfile
from django.http import Http404
# Create your views here.

def add_edu(request):
    if request.method == "GET":
        return render(request, "accounts/add-education.html")


def add_exp(request):
    if request.method == "GET":
        return render(request, "accounts/add-experience.html")

def create(request):
    if request.method == "GET":
        return render(request, "accounts/create-profile.html")

def dashboard(request):
    if request.method == "GET":
        return render(request, "accounts/dashboard.html")

def login(request):
   if request.method == "GET":
        return render(request, "accounts/login.html")

def profile(request):
    if request.method == "GET":
        return render(request, "accounts/profile.html")

def profiles(request):
    if request.method == "GET":
        try:
            all_profiles = UserProfile.objects.all()
        except UserProfile.DoesNotExist:
            raise Http404 ("UserProfile does not exist")
        return render(request, "accounts/profiles.html", context={"all_profiles":all_profiles})

def register(request):
    if request.method == "GET":
        return render(request, "accounts/register.html")


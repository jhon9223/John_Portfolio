from django.shortcuts import render
from .models import *

# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render
from .models import Profile


def home(request):
    profile = Profile.objects.first()  # get first profile
    return render(request, 'home.html', {'profile': profile})

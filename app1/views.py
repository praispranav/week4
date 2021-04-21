from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth import login, logout
# from django.contrib.auth.forms import

from .models import cardealer, carmodel
from .forms import reviewform


# Get an instance of a logger
logger = logging.getLogger(__name__)


# # # Create your views here.
# def index(request):
#     a = cardealer.objects.all()
#     context ={ 
#         'a':a
#     }
#     return render(request,"index2.html", context)


# Create an `about` view to render a static about page
def about(request):
    a = 0
    context= {
        "a":a
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')

def login_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request,user)
                return redirect('/car')

    context={
        "form": form
    }
    return render(request, 'login.html', context)

def registration_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
        return render(request, 'signup.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('/')

# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# # Update the `get_dealerships` view to render the index page with a list of dealerships
def index(request):
    ca = cardealer.objects.all()
    pran = "pranav"
    context={
        'ca': ca,
        'pran':pran
    }
    return render(request, 'index.html', context)

def detail(request, com_id):
    a = cardealer.objects.get(id=com_id)
    b = a.carmodel_set.all()
    form = reviewform()
    if request.method == 'POST':
        form= reviewform(request.POST)
        if b.is_valid:
            form.save()
    context={
        'b':b,
        'form':form
    }
    return render(request, 'detail.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...


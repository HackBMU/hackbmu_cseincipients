from travel.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from travel.forms import UserForm,UserProfileForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.test.utils import override_settings
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
# Create your views here.

def home(request):
    pass

@csrf_protect
@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return HttpResponseRedirect('/login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'travel/test_login.html', context_dict)

@csrf_protect
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(user.username)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect("Account Disabled")
        else:
            print("Invalid credentials: {0}, {1}".format(username, password))
            context_dict = {}
            context_dict['error'] = "Invalid login details"
            return render(request, 'travel/login.html', context_dict)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'travel/login.html', context_dict)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def profile(request):
    context_dict = {}
    user_details = list(UserProfile.objects.filter(user=request.user))
    for i in user_details:
        context_dict['name'] = i.name
        context_dict['college'] = i.college
        context_dict['contact'] = i.contact
        context_dict['picture'] = i.picture
        if i.gender == "0":
            context_dict['gender'] = "Female"
        elif i.gender == "1":
            context_dict['gender'] = "Male"
        elif i.gender == "2":
            context_dict['gender'] = "Other"
        context_dict['location'] = i.location
        context_dict['aadhar'] = i.aadhar_no
    context_dict['email'] = request.user.email
    obj = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST or None, instance=obj)
    context_dict['form'] = form
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.picture)
            if 'picture' in request.FILES:
                obj.picture = request.FILES['picture']
                print(request.FILES['picture'])
            obj.save()
            context_dict['form'] = form
            return HttpResponseRedirect('/profile')
        else:
            context_dict['form'] = form
            context_dict['error'] = 'The form was not updated successfully.'
            return render(request, 'website/profile1.html', context_dict)
    return render(request, 'travel/profile1.html', context_dict)

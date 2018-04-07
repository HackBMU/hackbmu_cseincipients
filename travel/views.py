from travel.models import UserProfile, Vendors, Vendor_services, user_services
from django.contrib.auth.models import User
from django import forms
from travel.forms import UserForm,UserProfileForm, TripPlannerForm, VendorTripPlannerForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.test.utils import override_settings
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    context_dict = {}
    return render(request, 'travel/Home.html', context_dict)


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
                users= UserProfile.objects.filter(user=user)
                if len(users)>0:
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/homeVendor')
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
        context_dict['gender'] = i.gender
        context_dict['location'] = i.location
        context_dict['aadhar'] = i.aadhar_no
    context_dict['email'] = request.user.email
    # obj = get_object_or_404(UserProfile, user=request.user)
    # form = UserProfileForm(request.POST or None, instance=obj)
    # context_dict['form'] = form
    # # if request.method == "POST":
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         print(obj.picture)
    #         if 'picture' in request.FILES:
    #             obj.picture = request.FILES['picture']
    #             print(request.FILES['picture'])
    #         obj.save()
    #         context_dict['form'] = form
    #         return HttpResponseRedirect('/profile')
    #     else:
    #         context_dict['form'] = form
    #         context_dict['error'] = 'The form was not updated successfully.'
    #         return render(request, 'website/profile1.html', context_dict)
    return render(request, 'travel/Profile.html', context_dict)


@csrf_protect
@csrf_exempt
@login_required(login_url='/login/')
def trip_planner(request):
    context_dict={}
    form = TripPlannerForm()
    context_dict['form']=form
    return render(request, 'travel/trip_planner.html', context_dict)

@login_required(login_url='/login/')
def trip_prev(request):
    context_dict = {}
    trips = list(user_services.objects.filter(username=request.user.username))
    context_dict['trip_details']=trips
    return render(request, 'travel/myPrevTrip.html', context_dict)

@login_required(login_url='/login/')
def user_input_result(request):
    context_dict = {}
    if request.method == 'POST':
        form = TripPlannerForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            seats_count = data['seats_need']
            date = data['date']
            time = data['time']
            source = data['source']
            destination = data['destination']
            vendors_filtered = list(Vendor_services.objects.all())
            vendors_filter=[]
            for i in vendors_filtered:
                if i.seats_count > seats_count:
                    if source == "BML":
                        if i.hop_bml:
                            if destination == "BML":
                                if i.hop_bml:
                                    vendors_filter.append(i)
                            elif destination == "Manesar":
                                if i.hop_manesar:
                                    vendors_filter.append(i)
                            elif destination == "Rajiv Chowk":
                                if i.hop_rajiv_chowk:
                                    vendors_filter.append(i)
                            if destination == "Iffco Chowk":
                                if i.hop_iffco_chowk:
                                    vendors_filter.append(i)
                    elif source == "Manesar":
                        if i.hop_manesar:
                            if destination == "BML":
                                if i.hop_bml:
                                    vendors_filter.append(i)
                            elif destination == "Manesar":
                                if i.hop_manesar:
                                    vendors_filter.append(i)
                            elif destination == "Rajiv Chowk":
                                if i.hop_rajiv_chowk:
                                    vendors_filter.append(i)
                            if destination == "Iffco Chowk":
                                if i.hop_iffco_chowk:
                                    vendors_filter.append(i)
                    elif source == "Rajiv Chowk":
                        if i.hop_rajiv_chowk:
                            if destination == "BML":
                                if i.hop_bml:
                                    vendors_filter.append(i)
                            elif destination == "Manesar":
                                if i.hop_manesar:
                                    vendors_filter.append(i)
                            elif destination == "Rajiv Chowk":
                                if i.hop_rajiv_chowk:
                                    vendors_filter.append(i)
                            if destination == "Iffco Chowk":
                                if i.hop_iffco_chowk:
                                    vendors_filter.append(i)
                    elif source == "Iffco Chowk":
                        if i.hop_iffco_chowk:
                            if destination == "BML":
                                if i.hop_bml:
                                    vendors_filter.append(i)
                            elif destination == "Manesar":
                                if i.hop_manesar:
                                    vendors_filter.append(i)
                            elif destination == "Rajiv Chowk":
                                if i.hop_rajiv_chowk:
                                    vendors_filter.append(i)
                            if destination == "Iffco Chowk":
                                if i.hop_iffco_chowk:
                                    vendors_filter.append(i)
            context_dict['vendors_filter']=vendors_filter
            context_dict['seats_need'] = seats_count
            context_dict['date'] = date
            context_dict['time'] = time
            context_dict['source'] = source
            context_dict['destination'] = destination
        else:
            print(form.errors)
    return render(request, 'travel/user_input_details.html', context_dict)

@login_required(login_url='/login/')
def save_user_services(request):
    context_dict = {}
    if request.method == 'POST':
        v_username = request.POST['vendor_username']
        v_no = request.POST['vehicle_no']
        date = request.POST['date']
        time = request.POST['time']
        n_seats = request.POST['num_seats']
        mot = request.POST['mot']
        source = request.POST['source']
        dest = request.POST['dest']
        price = request.POST['price']
        try:
            p= user_services(username=request.user.username,date=date,time=time,seats_need=n_seats,source=source,destination=dest
                         ,price=price,seats_count=n_seats,vehicle_no=v_no,transport_mode=mot,vendor_username=v_username)
            p.save()
            ven=Vendor_services.objects.get(username=v_username,date=date,time=time)
            ven.seats_count -= int(n_seats)
            ven.save()
            return render(request, 'travel/success.html', context_dict)
        except:
            pass
    return render(request, 'travel/user_input_details.html', context_dict)

@login_required(login_url='/login/')
def success(request):
    context_dict={}
    return render(request, 'travel/success.html', context_dict)

@login_required(login_url='/login/')
def emergency(request):
    context_dict = {}
    return render(request, 'travel/Emergency.html', context_dict)

@login_required(login_url='/login/')
def homeVendor(request):
    context_dict = {}
    return render(request, 'travel/homeVendor.html', context_dict)

@login_required(login_url='/login/')
def profileV(request):
    context_dict = {}
    user_details = list(Vendors.objects.filter(username=request.user.username))
    for i in user_details:
        context_dict['name'] = i.name
        context_dict['contact'] = i.contact
        context_dict['picture'] = i.picture
        context_dict['gender'] = i.gender
        context_dict['aadhar'] = i.aadhar_no
        context_dict['type'] = i.type
        context_dict['email'] = i.email
    return render(request, 'travel/ProfileV.html', context_dict)

@login_required(login_url='/login/')
def emergencyV(request):
    context_dict = {}
    return render(request, 'travel/EmergencyV.html', context_dict)

@login_required(login_url='/login/')
def myPrevTripV(request):
    context_dict = {}
    trips = list(Vendor_services.objects.filter(username=request.user.username))
    context_dict['trip_details'] = trips
    return render(request, 'travel/myPrevTripV.html', context_dict)

@login_required(login_url='/login/')
def contact(request):
    context_dict = {}
    return render(request, 'travel/contact.html', context_dict)

@login_required(login_url='/login/')
def contactV(request):
    context_dict = {}
    return render(request, 'travel/contactV.html', context_dict)

@login_required(login_url='/login/')
def registerTripVendor(request):
    context_dict = {}
    form = VendorTripPlannerForm()
    if request.method == 'POST':
        form = VendorTripPlannerForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.username=request.user.username
            hop1 = False
            if request.POST.get('group1') == "on":
                hop1 = True
            hop2 = False
            if request.POST.get('group2') == "on":
                hop2 = True
            hop3 = False
            if request.POST.get('group3') == "on":
                hop3 = True
            hop4 = False
            if request.POST.get('group4') == "on":
                hop4 = True
            data.hop_bml = hop1
            data.hop_manesar = hop2
            data.hop_rajiv_chowk = hop3
            data.hop_iffco_chowk = hop4
            data.save()
            print(data.username)
        else:
            print(form.errors)
    context_dict['form'] = form
    return render(request, 'travel/RegisterTripVendor.html', context_dict)
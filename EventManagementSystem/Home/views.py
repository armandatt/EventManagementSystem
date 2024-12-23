from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from .models import CustomUser, Event, Registration
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login


def home(request):
    return render(request, "home.html")


def ViewEvents(request):
    views = Event.objects.all()
    return render(request , "events.html" ,{"eventData": views})


def CreateEvents(request):
    if not request.session.get('is_admin'):
        messages.error(request, "Only admins can create events.")
        return redirect("Events")
    return render(request, "createEvent.html")

def insertEvent(request):
    event = Event(
        event_name=request.POST.get('event_name'),
        start_date=request.POST.get('start_date'),
        end_date=request.POST.get('end_date'),
        event_date=request.POST.get('event_date'),
        event_location=request.POST.get('event_location'),
        fees=request.POST.get('fees')
    )
    event.save()
    return redirect("Success")

def deleteEvent(request, event_id):
    event = Event.objects.get(event_id = event_id)
    event.delete()
    return render(request , "DeleteEvent.html")

def UpdateEvent(request, event_id):
    if not request.session.get('is_admin'):
        messages.error(request, "Only admins can update events.")
        return redirect("Events")
    
    event = get_object_or_404(Event, event_id=event_id)
    return render(request, "UpdateEvent.html", {'event': event})

def EditEvent(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    event.event_name = request.POST.get('event_name')
    event.start_date = request.POST.get('start_date')
    event.end_date = request.POST.get('end_date')
    event.event_date = request.POST.get('event_date')
    event.event_location = request.POST.get('event_location')
    event.fees = request.POST.get('fees')
    event.save()
    return redirect("Events")

def LoginUser(request):
    return render(request, "login.html")

def CheckUser(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        # Attempt to get user by email
        user = CustomUser.objects.get(email=email)
        if check_password(password, user.password):
            # Set session data for the user and login the user explicitly
            login(request, user)  # Ensure user is logged in and session is set
            request.session['is_logged_in'] = True
            request.session['user_id'] = user.user_id
            request.session['username'] = user.username
            request.session['is_admin'] = user.is_admin


            return redirect("Home") 

        else:
            messages.error(request, "Login failed: Incorrect password.")
            return render(request, "login.html")

    except CustomUser.DoesNotExist:
        messages.error(request, "Login failed: Email not registered.")
        return render(request, "login.html")

def RegisterUser(request):
    return render(request, "signup.html")

def CreateUser(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if CustomUser.objects.filter(email=email).exists():
        messages.error(request, 'Email already exists.')
        return redirect("RegisterUser")
    
    user = CustomUser(username=username, email=email, password=make_password(password))
    user.save()
    messages.success(request, 'User registered successfully!')
    return redirect("LoginUser")

def logout_CustomUser(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect("LoginUser")


def ContactUs(request):
    return render(request, "Contact.html")

def AboutUs(request):
    return render(request, "About.html")

def SuccessPage(request):
    return render(request, "successPage.html")


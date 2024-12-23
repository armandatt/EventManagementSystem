from django.urls import path
from Home.views import *


urlpatterns = [
    # Home and General Pages
    path('', home, name="Home"),
    path('home', home, name="Home"),
    path('Contact', ContactUs, name="ContactUs"),
    path('About', AboutUs, name="AboutUs"),
    path('success', SuccessPage, name="Success"),

    # Event Management
    path('events', ViewEvents, name="Events"),
    path('createEvent', CreateEvents, name="CreateEvents"),
    path('insertEvent', insertEvent, name="InsertEvent"),
    path('DeleteEvent/<int:event_id>/', deleteEvent, name="DeleteEvent"),
    path('UpdateEvent/<int:event_id>/', UpdateEvent, name="UpdateEvent"),
    path('EditEvent/<int:event_id>', EditEvent, name="EditEvent"),

    # User Authentication
    path('login', LoginUser, name="LoginUser"),
    path('register', RegisterUser, name="RegisterUser"),
    path('CreateUser', CreateUser, name="CreateUser"),
    path('CheckUser', CheckUser, name="CheckUser"),
    path('logout', logout_CustomUser, name="logout_user"),

] 



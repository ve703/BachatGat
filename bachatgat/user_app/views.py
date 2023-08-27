from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from admin_app.models import profile
# import view sets from the REST framework
from rest_framework import viewsets

from .forms import UserLoginForm
 
# import the LoginSerializer from the serializer file
from .serializers import LoginSerializer


def home(request):
   return render(request, 'index.html')

from django.contrib.auth.backends import ModelBackend
from admin_app.models import profile  # Import your Profile model

# class ProfileModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             profile = profile.objects.get(username=username)  # Replace with appropriate lookup
#             if profile.check_password(password):
#                 return redirect("home")
#   # Assuming your Profile model has a OneToOneField to User
#         except profile.DoesNotExist:
#             return None

    # def get_user(self, user_id):
    #     try:
    #         return profile.objects.get(user_id=user_id).id
    #     except profile.DoesNotExist:
    #         return None

def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid User or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "login.html", context)
# Create your views here.
# create a class for the Todo model viewsets
class LoginView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = LoginSerializer
 
    # define a variable and populate it
    # with the Todo list objects
    queryset = profile.objects.all()
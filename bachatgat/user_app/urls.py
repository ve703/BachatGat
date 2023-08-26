from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    # path('login/', views.ProfileModelBackend, name='login'),
    path('home/', views.home, name='home'),
]


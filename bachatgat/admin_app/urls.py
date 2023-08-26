from django.urls import path
from . import views

urlpatterns = [
    path('app_admin/', views.admin_app, name='admin_app'),
    path('app_admin/register/', views.register_member, name='register'),
    path('app_admin/sucess/', views.registration_sucess, name='sucess'),
    path('app_admin/members/', views.memberlist, name='members'),
    path('app_admin/members_details/', views.memberdetails, name='members_details'),
    path('schedule_meet/', views.schedule_meet, name='schedule_meet'),
]


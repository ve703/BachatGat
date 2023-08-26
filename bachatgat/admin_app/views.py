from django.shortcuts import render , redirect
from django.http import HttpResponse
from .form import UserRegistrationForm
from .models import profile
from django.conf import settings
from django.core.mail import send_mail

 

#def admin_app(request):
#    template = loader.get_template('firstpage.html')
#    return HttpResponse(template.render)

def admin_app(request):
   return render(request, 'firstpage.html')


def registration_sucess(request):
   return render(request, 'sucess.html')    

def memberlist(request):
   member_data=profile.objects.all()
   context = {
    'mymembers': member_data,
   }
   return render(request, 'member_list.html',context)  

def memberdetails(request):
   member_info=profile.objects.all()
   context = {
    'members': member_info,
   }
   return render(request, 'member_details.html',context)  

def register_member(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form.clear_form_data()
            return redirect('sucess')  # Create a success view
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def schedule_meet(request):
   subject = 'welcome to GFG world'
   message = f'Hi {profile.username}, thank you for registering in geeksforgeeks.'
   email_from = settings.EMAIL_HOST_USER
   recipient_list = [profile.email]
   send_mail( subject, message, email_from, recipient_list) 
   return render(request, 'firstpage.html')


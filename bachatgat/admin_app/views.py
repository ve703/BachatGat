from django.shortcuts import render , redirect
from django.http import HttpResponse
from .form import UserRegistrationForm
from .models import profile
from django.conf import settings
from django.core.mail import send_mail
from .meeting_form import MeetingEventForm
from .models import MeetingEvent
from .attendance_form import AttendanceForm




 

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
   email_records = profile.objects.all()
   subject = 'welcome to GFG world'

   for email_record in email_records:
        message = f'Hi {email_record.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_record.email]  # Send email to the user's email address
        send_mail(subject, message, email_from, recipient_list)
    
   return render(request, 'firstpage.html')


def schedule_event(request):
    if request.method == 'POST':
        form = MeetingEventForm(request.POST)
        if form.is_valid():
            form.save()
            form.clear_form_data()
            # meeting_event.meeting_id = request.user  # Assign the logged-in user as the meeting organizer
            # meeting_event.save()
            return redirect('event_list')  # Redirect to a page that lists events
    else:
        form = MeetingEventForm()
    return render(request, 'schedule_event.html', {'meeting_form': form})
  

def event_list(request):
    events = MeetingEvent.objects.all()
    context = {
    'scheduled_events': events,
   }
    return render(request, 'event_list.html', context)

# def mark_attendance_popup(request, meeting_id):
#     meeting = Attendance.objects.get(pk=meeting_id)

#     if request.method == 'POST':
#         # for attendee in meeting.attendees.all():
#             # is_present = request.POST.get(f'attendance_{attendee.id}', False)
#             # attendee.present = is_present
#             # attendee.save()
#         return redirect('meeting_details', meeting_id=meeting_id)

#     return redirect('meeting_details', meeting_id=meeting_id)

def mark_attendance(request,meeting_id):
    meeting = MeetingEvent.objects.get(pk=meeting_id)
    # attendees = meeting.attendees.all()
    # member_name = profile.objects.get(pk=account_no)

    if request.method == 'POST':
        formset = AttendanceForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('meeting_list')  # Redirect to a list of meetings
    else:
        # initial_data = [{'meeting_id': meeting, 'account_no': attendee} for attendee in attendees]
        # form = MeetingEventForm()
        formset = AttendanceForm()

    return render(request, 'mark_attendance.html', {'attendance_form': formset})



from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100,primary_key = True)
    # account_no = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=100,default='Your Default Address')
    email = models.EmailField(max_length=100,default='Your Default Address')
    mobile = models.CharField(max_length=100,default='Your Default Address')
    username = models.CharField(max_length=100,default='Your Default Address')
    password = models.CharField(max_length=100,default='Your Default Address')
    birthday = models.DateField()
    address = models.CharField(max_length=100,default='Your Default Address')
    city = models.CharField(max_length=100,default='Your Default Address')
    state = models.CharField(max_length=100,default='Your Default Address')
    zip = models.CharField(max_length=100,default='Your Default Address')

    def __str__(self):
        return f"{self.name} - {self.account_no}"

class MeetingEvent(models.Model):
    meeting_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_place = models.CharField(max_length=200,default='Your usual meeting Address')
    # attendees = models.ManyToManyField(profile, through='Attendance', through_fields=('meeting_id', 'account_no'))


    def __str__(self):
        return f"{self.title}- {self.meeting_id}" 
    
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    account_no = models.ForeignKey(profile, on_delete=models.CASCADE)
    # name = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='attendees_name')
    # meeting_id = models.ForeignKey(MeetingEvent, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.id # You might want to adjust this depending on the structure of your Profile model

# attendance_choices = (
#     ('absent', 'Absent'),
#     ('present', 'Present')
# )

# class Attendance(models.Model):
#     name = models.ForeignKey('profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='attendees_name')
#     account_no = models.ForeignKey('profile', on_delete=models.CASCADE, related_name='attendees_accountNo',)
#     meeting_id = models.ForeignKey('MeetingEvent', on_delete=models.CASCADE, )
#     attendance = models.CharField(max_length=8, choices=attendance_choices, blank=True)

#     def __str__(self):
#         return f"{self.account_no}"
    

    
#class accounts(models.Model):


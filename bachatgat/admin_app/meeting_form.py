from django import forms
from django.contrib.auth.models import User
from .models import MeetingEvent
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class MeetingEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter purpose of meeting'}))
    meeting_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31', 'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 13:00:00', 'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 14:00:00', 'type': 'time'}))
    meeting_place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your usual meeting place'}))

    def clear_form_data(self):
        # Clear the form data
        self.cleaned_data = {}
        
    class Meta:
        model = MeetingEvent
        fields = ['title', 'meeting_date', 'start_time', 'end_time', 'meeting_place']
        widgets = {
            'meeting_date': AdminDateWidget(),
            'start_time': AdminTimeWidget(),
            'end_time': AdminTimeWidget(),
        }
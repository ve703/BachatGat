from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    is_present = forms.BooleanField( widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Attendance
        fields = ['id','account_no','is_present']
        
# 'account_no', 'name','meeting_id'
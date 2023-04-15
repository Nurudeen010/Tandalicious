from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tanda

class TandaForm(forms.ModelForm):
    class Meta:
        model = Tanda
        fields = ['email', 'complaintType', 'complaintDetails', 'recommendation']
    

Complaint_choices = (
    ('issue with staff', 'ISSUE WITH STAFF'),
    ('issue with food', 'ISSUE WITH FOOD'),
    ('both', 'BOTH'),
)


class NewStaffForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['email'].label = 'Email'
        self.fields['username'].label = 'Username'

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {
            'username': None,
        }
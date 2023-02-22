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


class TindaForm(forms.Form):
    email = forms.EmailField(max_length=254)
    complaintType = forms.CharField(max_length=50)
    complaintDetails = forms.CharField(max_length=300)
    recommendation = forms.CharField(max_length=300)    


class NewStaffForm(UserCreationForm):
    email = forms.EmailField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewStaffForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
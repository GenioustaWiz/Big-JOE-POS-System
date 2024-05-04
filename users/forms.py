from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


User_choices = [
    ('',''),
    ('yes','yes'),
    ('no','no'),
]

class CustomUserCreationForm(UserCreationForm):
    is_admin =forms.CharField(label='Admin', widget=forms.Select(choices=User_choices))

    class Meta(UserCreationForm.Meta):  
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('fullname', 'phone_no', 'is_admin', 'id_no',)
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
from django import forms
from .models import SmsDetail, ContactDetail
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class SmsDetailForm(forms.Form):
    to = forms.CharField(max_length=15)
    message_body = forms.CharField(max_length=160, required="True")

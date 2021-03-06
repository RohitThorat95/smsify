from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.conf import settings

phone_regex = RegexValidator(
    regex=r'^(\+?1?\d{10})|(\+?1?\d{13})$', message="Phone number must be entered in the format: '+999999999'. 10 digits allowed.")
# Create your models here.

#User._meta.get_field('email')._unique = True

count = models.IntegerField(default=10)
count.contribute_to_class(User, 'smscount')


class ContactDetail(models.Model):
    user = models.ForeignKey(User, default=1)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_num = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["-id"]


class SmsDetail(models.Model):
    to = models.CharField(
        validators=[phone_regex], max_length=15, null=True, blank=True)
    user = models.ForeignKey(User, default=1)
    contact = models.ForeignKey(
        ContactDetail, on_delete=models.CASCADE, null=True, blank=True)
    message_body = models.CharField(
        max_length=160, help_text='Max Charecter length: 160')

    def get_absolute_url(self):
        return reverse('smsdetails:message', kwargs={'pk': self.pk})

    def __str__(self):
        if self.contact is not None:
            return self.contact.first_name + " " + self.message_body
        else:
            return self.to + " " + self.message_body

    class Meta:
        ordering = ["-id"]

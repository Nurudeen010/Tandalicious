from django.db import models
from django import forms
from PIL import Image


Complaint_choices = (
    ('issue with staff', 'ISSUE WITH STAFF'),
    ('issue with food', 'ISSUE WITH FOOD'),
    ('both', 'BOTH'),
) 


class Tanda(models.Model):
    email = models.EmailField(max_length=40, blank=False)
    complaintType = models.CharField(max_length= 20, choices=Complaint_choices, default='issue with staff')
    complaintDetails = models.TextField(max_length=200, default='Write your complaints here')
    recommendation = models.TextField( max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email

class Gallery(models.Model):
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='gallery/', null=True)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title

from django.db import models

Complaint_choices = (
    ('issue with staff', 'ISSUE WITH STAFF'),
    ('issue with food', 'ISSUE WITH FOOD'),
    ('both', 'BOTH'),
) 


class Tanda(models.Model):
    email = models.EmailField(max_length=254)
    complaintType = models.CharField(max_length=50, choices=Complaint_choices, default='issue with staff')
    complaintDetails = models.TextField(default='lodge your complaint here')
    recommendation = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email


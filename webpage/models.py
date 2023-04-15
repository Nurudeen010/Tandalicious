from django.db import models

Complaint_choices = (
    ('issue with staff', 'ISSUE WITH STAFF'),
    ('issue with food', 'ISSUE WITH FOOD'),
    ('both', 'BOTH'),
) 


class Tanda(models.Model):
    email = models.EmailField(max_length=40, blank=False)
    complaintType = models.CharField(max_length=20, choices=Complaint_choices, default='issue with staff')
    complaintDetails = models.TextField(max_length=80, default='lodge your complaints here')
    recommendation = models.TextField( max_length=80, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email


from __future__ import unicode_literals
import datetime
from django.urls import reverse
from django.db import models
import jsonfield


class UserModel(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField(primary_key=True)
    contact_no=models.PositiveIntegerField()

    def __str__(self):
        return self.email

class DonationModel(models.Model):
    donor=models.CharField(max_length=100)
    donor_address=models.TextField()
    donor_email= models.EmailField()
    donor_contact=models.IntegerField(default=00)
    donation_items=jsonfield.JSONField()
    receiver=models.CharField(max_length=100)
    receiver_address=models.TextField()
    receiver_email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail-donations',args=[str(self.id)])




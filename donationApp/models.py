from __future__ import unicode_literals
import datetime
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
    donor=models.ForeignKey(UserModel,related_name='donor')
    donor_address=models.TextField()
    donation_items=jsonfield.JSONField()
    receiver=models.ForeignKey(UserModel,related_name='receiver')
    receiver_address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)



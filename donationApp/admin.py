from django.contrib import admin
from .models import UserModel,DonationModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(DonationModel)
from __future__ import unicode_literals

import jsonfield
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,name,address,contact_no,is_receiver):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.name = name
        user.address = address
        user.contact_no = contact_no
        user.is_receiver = is_receiver
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class UserModel(AbstractBaseUser):
    email=models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.CharField(max_length=10)
    is_receiver = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name','address','contact_no','is_receiver']
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class DonationModel(models.Model):
    donor=models.CharField(max_length=100)
    donor_address=models.TextField()
    donor_email= models.EmailField()
    donor_contact=models.IntegerField(default=00)
    donation_items=jsonfield.JSONField()
    receiver=models.CharField(max_length=100)
    receiver_contact=models.IntegerField(default=00)
    receiver_email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail-donations',args=[str(self.id)])
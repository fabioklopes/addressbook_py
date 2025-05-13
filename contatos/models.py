from django.contrib.auth import user_logged_in
from django.db import models

class SystemUser(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    temp_password = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    class Meta:
        ordering = ['name']
        
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=15, unique=True, blank=False, null=False)
    active = models.BooleanField(default=True)

    created_by = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
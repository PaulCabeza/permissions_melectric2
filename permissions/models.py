from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Permission(models.Model):
    permission_number = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    issued_date = models.DateTimeField()
    issued_by = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    

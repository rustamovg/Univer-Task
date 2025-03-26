from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name = models.CharField("Full name", max_length=250)
    email = models.EmailField("Email", unique=True)
    phone_number = PhoneNumberField("Phone number", null=False, blank=False, unique=True, region="UZ")

    def __str__(self):
        return self.name
    
class Question(models.Model):
    name = models.CharField("Full name", max_length=250)
    email = models.EmailField("Email", unique=True)
    message = models.TextField("Question")

    def __str__(self):
        return self.name
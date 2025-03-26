from django import forms
from .models import User, Question
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    phone_number = PhoneNumberField(region="UZ")
    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number'] 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'message']
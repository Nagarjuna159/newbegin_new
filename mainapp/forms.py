from django import forms
from .models import Contact_Model, Enquire_Course_Model, Quiz
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = ("full_name","email","phone","contacting_for","message")

class Enquire_Course_Form(forms.ModelForm):
    class Meta:
        model = Enquire_Course_Model
        fields = ("name","select_course","email","phone")

class Quiz_form(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('question','choice_one','choice_two','choice_three','choice_four','answer')
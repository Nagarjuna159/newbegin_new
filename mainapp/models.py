from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
Contacting_For_Choices = [
    ('Please Choose','Please Choose'),
    ('Training','Training'),
    ('Web Applications','Web Applications'),
    ('Android/IOS Apps','Android/IOS Apps')
]
 
Enquire_Course_Choices = [
    ("Python Web Development","Python Web Development"),
    ("Java Web Development","Java Web Development"),
    ("Full Stack Training","Full Stack Training"),
    ("Java & Python","Java & Python"),
]


class Contact_Model(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    contacting_for = models.CharField(max_length=30,choices=Contacting_For_Choices,default="Please Choose")
    message = models.TextField()


class Enquire_Course_Model(models.Model):
    name = models.CharField(max_length=60)
    select_course = models.CharField(max_length=30,choices=Enquire_Course_Choices,default="Python Web Development")
    email = models.EmailField()
    phone = models.IntegerField()

    


class Quiz(models.Model):
    question = models.CharField(max_length=500)
    choice_one = models.CharField(max_length=60)
    choice_two = models.CharField(max_length=60)
    choice_three = models.CharField(max_length=60)
    choice_four = models.CharField(max_length=60)
    answer = models.CharField(max_length=60)
    
    

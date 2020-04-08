from django.contrib import admin
from .models import Contact_Model, Enquire_Course_Model,Quiz
# Register your models here.
class Contact_admin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','contacting_for']

class Enquire_Course_Admin(admin.ModelAdmin):
    list_display = ['name','select_course','email','phone']



admin.site.register(Contact_Model,Contact_admin)
admin.site.register(Enquire_Course_Model,Enquire_Course_Admin)
admin.site.register(Quiz)

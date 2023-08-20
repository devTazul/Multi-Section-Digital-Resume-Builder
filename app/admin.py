from django.contrib import admin
from .models import  PersonalInformation,Education,WorkExperience
# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(Education)
admin.site.register(WorkExperience)

from django.db import models


class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    graduation_year = models.PositiveIntegerField()


class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

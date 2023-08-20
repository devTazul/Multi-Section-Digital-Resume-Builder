from django import forms
from .models import PersonalInformation, Education, WorkExperience

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['full_name', 'email', 'phone_number']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'graduation_year']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'position', 'start_date', 'end_date']

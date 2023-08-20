from django.urls import path
from .views import personal_information_view, education_view, work_experience_view, preview_resume_view,generate_pdf_view

urlpatterns = [
    path('personal_information/', personal_information_view, name='personal_information'),
    path('education/', education_view, name='education'),
    path('work_experience/', work_experience_view, name='work_experience'),
    path('preview_resume/', preview_resume_view, name='preview_resume'),
    path('generate_pdf/', generate_pdf_view, name='generate_pdf'),
]

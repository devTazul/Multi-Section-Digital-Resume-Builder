from django.shortcuts import render, redirect
from .forms import PersonalInformationForm, EducationForm, WorkExperienceForm
from .models import PersonalInformation, Education, WorkExperience
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse


# Create your views here.


def personal_information_view(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education')  # Redirect to the next section
    else:
        form = PersonalInformationForm()
    return render(request, 'personal_information_form.html', {'form': form})


def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_experience')  # Redirect to the next section
    else:
        form = EducationForm()
    return render(request, 'education_form.html', {'form': form})


def work_experience_view(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preview_resume')  # Redirect to the resume preview
    else:
        form = WorkExperienceForm()
    return render(request, 'work_experience_form.html', {'form': form})


def preview_resume_view(request):
    # Retrieve the saved resume data and render the preview template
    return render(request, 'preview_resume.html')


def generate_pdf_view(request):
    # Retrieve the saved resume data
    personal_info = PersonalInformation.objects.last()
    education = Education.objects.last()
    work_experience = WorkExperience.objects.last()

    # Create a response object to return the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'

    # Create a PDF using ReportLab
    # This is Personal Information section
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Personal Information:")
    p.drawString(100, 730, f"Name: {personal_info.full_name}")
    p.drawString(100, 710, f"Email: {personal_info.email}")
    p.drawString(100, 690, f"Phone: {personal_info.phone_number}")
    p.showPage()
    p.save()
    # Similar code for Education and Work Experience sections

    # This is Education section
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Education:")
    p.drawString(100, 730, f"Institution: {education.institution}")
    p.drawString(100, 710, f"Degree: {education.degree}")
    p.drawString(100, 690, f"Year: {education.graduation_year}")
    p.showPage()
    p.save()

    # This is Work_Experience section
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Work Experience:")
    p.drawString(100, 730, f"Company: {work_experience.company}")
    p.drawString(100, 710, f"Position: {work_experience.position}")
    p.drawString(100, 690, f"Start Date: {work_experience.start_date}")
    p.drawString(100, 690, f"End Date: {work_experience.end_date}")

    p.showPage()
    p.save()

    return response

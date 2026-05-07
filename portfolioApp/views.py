from django.shortcuts import render, get_object_or_404
from .models import (
    Profile,
    Skill,
    Project,
    Experience,
    Education,
    Certification
)


def home(request):
    #  Profile (single)
    profile = Profile.objects.first()

    #  Skills
    skills = Skill.objects.all()

    #  Projects
    projects = Project.objects.all().order_by('-created_at')

    #  Featured Projects (optional use)
    featured_projects = Project.objects.filter(is_featured=True)

    #  Experience
    experiences = Experience.objects.all().order_by('-start_date')

    #  Education
    educations = Education.objects.all()

    #  Certifications
    certifications = Certification.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'featured_projects': featured_projects,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
    }

    return render(request, 'home.html', context)


#  PROJECT DETAIL PAGE (VERY IMPORTANT FOR PRO LEVEL)
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(request, 'project_detail.html', {
        'project': project
    })

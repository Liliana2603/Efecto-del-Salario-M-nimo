from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    # pylint: disable=E1101
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


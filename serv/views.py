from django.shortcuts import render
from .models import Project
# Create your views here.
def services(request):
    context = {'serv': 'active'}
    return render(request, 'serv/services.html',context)


def projects(request):
    project = Project.objects.all()

    context = {
        'proj': 'active',
        'project': project
        
        }

    return render(request, 'serv/projects.html',context)
from django.shortcuts import render
from .models import info, Projects


# Create your views here.
def home(request):
    Info = info.objects.all()
    project = Projects.objects.all()  # Fix: Call the queryset with ()
    context = {
        'Info': Info,
        'Project': project,  # Fix: Use the correct variable here (project)
    }
    return render(request, "index.html", context)
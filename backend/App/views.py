from django.shortcuts import render
from .models import info, Projects


# Create your views here.
def home(request):
    # info = info.objects.all()
    Info = info.objects.all()
    project = Projects.objects.all
    context = {
        'Info': info,
        'project': Projects,
        }
    return render(request, "index.html", context)
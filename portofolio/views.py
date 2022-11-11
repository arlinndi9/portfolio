from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PersonalInformation,About,Project
from .forms import Contact
# Create your views here.
def home(request):
    personalinfo=PersonalInformation.objects.all()
    context={
        'personalinfo':personalinfo
    }
    return render(request,'home.html',context)

def about(request):
    about=About.objects.all()
    context={
        'about':about
    }
    return render(request,'about.html',context)

def project(request):
    project=Project.objects.all()
    context={
        'project':project
    }
    return render(request, 'project.html', context)
def contact(request):
    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'contact.html', {'form': Contact})



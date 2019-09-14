from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
	jobs = Job.objects # take objects of Job module and save into jobs variable
	return render(request,'home.html', {'jobs':jobs})

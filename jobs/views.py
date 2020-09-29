from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView

from jobs.models import Job


class HomeView(ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'
    model = Job

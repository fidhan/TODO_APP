from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.

def addTask(request):
    taskName = (request.POST['task'])
    Task.objects.create(task=taskName)
    return redirect('home')
    
    return HttpResponse('the form is submitted')

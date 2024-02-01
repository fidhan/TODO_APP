from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib import messages
# Create your views here.

def addTask(request):
    taskName = (request.POST['task'].strip())
    if(taskName == ""):
        messages.error(request, 'Task name cannot be empty.')
        return redirect('home')
    Task.objects.create(task=taskName)
    return redirect('home')
    
def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if(request.method=='POST'):
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task':task
        }
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

    




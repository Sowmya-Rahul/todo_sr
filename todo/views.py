from .models import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    #return HttpResponse('The form is submitted')
    return redirect('home')
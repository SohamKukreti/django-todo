from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from .models import Task
# Create your views here.
def index(request):
    t = Task.objects.order_by("-created_at")
    return render(request, "todo/index.html", {"tasks" : t})

def add(request):
    if(request.POST["task_name"] == ""):
        return render(request, "todo/add.html", {"error_message" : "Please Enter the name of the task."})
    elif(request.POST["task_description"] == ""):
        return render(request, "todo/add.html", {"error_message" : "Please Enter the description of the task."})
    else:
        task = Task.objects.create(task_name = request.POST["task_name"],task_description = request.POST["task_description"], created_at = timezone.now())
        task.save()
        return HttpResponseRedirect(reverse("todo:index"))

def delete(request, pk):
    task = Task.objects.get(pk = pk)
    task.delete()
    return HttpResponseRedirect(reverse("todo:index"))

def info(request):
    return render(request, "todo/add.html")

def edit(request, pk):
    task = Task.objects.get(pk = pk)
    return render(request, "todo/edit.html", {"task" : task})

def modify_value(request, pk):
    task = Task.objects.get(pk = pk)
    if(request.POST["task_name"] == ""):
        return render(request, "todo/add.html", {"error_message" : "Please Enter the name of the task."})
    elif(request.POST["task_description"] == ""):
        return render(request, "todo/add.html", {"error_message" : "Please Enter the description of the task."})
    else:
        task.task_name = request.POST["task_name"]
        task.task_description = request.POST["task_description"]
        task.save()
        return HttpResponseRedirect(reverse("todo:index"))
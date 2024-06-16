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
    task = Task.objects.create(task_name = request.POST["task_name"], created_at = timezone.now())
    task.save()
    return HttpResponseRedirect(reverse("todo:index"))

def delete(request, pk):
    return HttpResponse("You are deleting task %s" % pk)

def info(request):
    return render(request, "todo/add.html")
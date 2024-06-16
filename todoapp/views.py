from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet
from .models import Task
# Create your views here.
def index(request):
    t = Task.objects.order_by("-created_at")
    return render(request, "todo/index.html", {"tasks" : t})

def add(request):
    return HttpResponse("You are at add page")

def delete(request, pk):
    return HttpResponse("You are deleting task %s" % pk)
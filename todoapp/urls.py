from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name = "index"),
    path("add/", views.add, name = "add"),
    path("<int:pk>/delete/", views.delete, name = "delete"),
    path("get_task_info/", views.info, name = "get_task_info"),
    path("<int:pk>/edit/", views.edit, name = "edit"),
    path("<int:pk>/modify/", views.modify_value, name = "modify")
]
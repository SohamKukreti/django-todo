from django.db import models
from django.utils import timezone
class Task(models.Model):
    task_name = models.CharField(max_length = 300)
    task_description = models.CharField(max_length = 600, default = "This is a normal task")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.task_name
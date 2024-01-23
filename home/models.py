from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_todos():
        return Todo.objects.all().order_by('-id')
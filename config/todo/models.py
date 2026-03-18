from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_FIELDS = [
        ('panding', 'PANDING'),
        ('fullfilled', 'FULLFILLED'),
        ('rejected', 'REJECTED')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_FIELDS, default='panding')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

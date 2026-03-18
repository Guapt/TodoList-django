from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.register(Todo)

class TodoAdmin(admin.ModelAdmin):
    list_display= ['title', 'description', 'status', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'status', 'created_at', 'updated_at']
    list_filter = ['title', 'description', 'status', 'created_at', 'updated_at']

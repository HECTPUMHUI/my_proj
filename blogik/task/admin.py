from django.contrib import admin
from .models import Task, Category


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated', 'completed']


admin.site.register(Category)

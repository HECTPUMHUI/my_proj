from django import forms

from .models import *


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Task Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Description')
    completed = forms.BooleanField(required=False, initial=True, label='Completed')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label="Category not choised")


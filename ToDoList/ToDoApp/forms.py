from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
	"""class to create a form to provide the task details"""

	title = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Task title...'}), label=False)
	due = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Due date...'}), label=False)

	class Meta:
		model = Task
		fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
	""" class to update the task which is created """

	title = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder': 'Task title...'}))

	class Meta:
		model = Task
		fields = ['title', 'due', 'complete']

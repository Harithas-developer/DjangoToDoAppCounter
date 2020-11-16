from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm

# Create your views here.


def listTask(request):
	""" Function to list all the tasks in the ToDoList"""

	queryset = Task.objects.order_by('complete', 'due')
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {
            'tasks': queryset,
          		'form': form,
        }
	return render(request, 'list_task.html', context)


def updateTask(request, pk):
	""" Function which performs the updation of the tasks in the todolist"""

	queryset = Task.objects.get(id=pk)
	form = UpdateForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
            'form': form
        }

	return render(request, 'update_task.html', context)


def deleteTask(request, pk):
	""" Function which is used to delete the task"""

	queryset = Task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
            'item': queryset
        }
	return render(request, 'delete_task.html', context)

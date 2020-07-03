from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm

def index(request):
	return render(request, 'app.html')


def task(request):
	task = Task.objects.all()
	return render(request, 'task.html', {'task':task})

def create_user(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Форма была не верной'	
	form = TaskForm()
	context = {
		'form':form,
		'error':error

	}
	return render(request, 'create_user.html', context)	
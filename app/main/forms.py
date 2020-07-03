from .models import Task

from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'intro']
		widgets = {
			'title' : TextInput(attrs={'class':'form-control', 'placeholder':'Введите название'}),
			'intro' : Textarea(attrs={'class':'form-control', 'placeholder':'Введите описание'})
		}
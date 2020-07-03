from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'home'),
	path('task/', views.task, name = 'task'),
	path('create_user/', views.create_user, name = 'create-user')
]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Priority
import datetime
from itertools import chain
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signIn(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('TodoList')
		else:
			messages.info(request, 'Username OR Password is incorrect.')

	context = {}
	return render(request, 'signIn.html', context)

def signUp(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request, 'signUp.html', context)

def signOut(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def index(request):
	curr_user = request.user.id
	todosNotDone = TodoList.objects.filter(status = 0, created_by = curr_user, due_date__gte = datetime.date.today())
	todosDue = TodoList.objects.filter(status = 0, created_by = curr_user, due_date__lt = datetime.date.today())
	todosDone = TodoList.objects.filter(status = 1, created_by = curr_user)
	todos = chain(todosNotDone,todosDue,todosDone)
	priorities = Priority.objects.all()
	taskEditId,taskEditValue,priorityEditValue,dateEditValue = "","","",""
	if request.method == "POST":
		if "taskAdd" in request.POST:
			title = request.POST["description"]
			date = str(request.POST["date"])
			priority = request.POST["priority_select"]
			content = title + " -- " + date + " " + priority
			if request.POST["id"]!="":
				todo = TodoList.objects.get(id=int(request.POST["id"]))
				todo.created_by = curr_user
				todo.title = title
				todo.due_date = date
				todo.priority = Priority.objects.get(name=priority)
				todo.content = content
				todo.save()
			else:
				Todo = TodoList(created_by=curr_user,title=title, content=content, due_date=date, priority=Priority.objects.get(name=priority))
				Todo.save()
			return redirect("/")

		if "taskEdit" in request.POST:
			checkedlist = request.POST.get("checkedbox")
			try:
				todo = TodoList.objects.get(id=int(checkedlist), created_by = curr_user)
				taskEditId = todo.id
				taskEditValue = todo.title
				priorityEditValue = todo.priority
				dateEditValue = todo.due_date
			except:
				pass

		if "taskDone" in request.POST:
			checkedlist = request.POST.getlist("checkedbox")
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id),created_by = curr_user)
				todo.status = 1
				todo.save()

		if "taskDelete" in request.POST:
			checkedlist = request.POST.getlist("checkedbox")
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))
				todo.delete()
	context = { "taskEditId":taskEditId,
				"taskEditValue":taskEditValue,
				"priorityEditValue":priorityEditValue,
				"dateEditValue":dateEditValue,
				"todos": todos,
				"priorities":priorities,
				"today":datetime.date.today()
			  }
	return render(request, "index.html",context)

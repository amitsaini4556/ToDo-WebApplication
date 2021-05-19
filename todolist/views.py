# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
import datetime
from itertools import chain
# Create your views here.

def index(request):
	todosNotDone = TodoList.objects.filter(status = 0)
	todosDone = TodoList.objects.filter(status = 1)
	todos = chain(todosNotDone,todosDone)
	categories = Category.objects.all()
	taskEditId,taskEditValue,categoryEditValue,dateEditValue = "","","",""
	if request.method == "POST":
		if "taskAdd" in request.POST:
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category_select"]
			content = title + " -- " + date + " " + category
			if request.POST["id"]!="":
				todo = TodoList.objects.get(id=int(request.POST["id"]))
				todo.title = title
				todo.due_date = date
				todo.category = Category.objects.get(name=category)
				todo.content = content
				todo.save()
			else:
				Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
				Todo.save()
			return redirect("/")

		if "taskEdit" in request.POST:
			checkedlist = request.POST.get("checkedbox")
			try:
				todo = TodoList.objects.get(id=int(checkedlist))
				taskEditId = todo.id
				taskEditValue = todo.title
				categoryEditValue = todo.category
				dateEditValue = todo.due_date
				print(dateEditValue)
				print(taskEditId)
			except:
				pass

		if "taskDone" in request.POST:
			checkedlist = request.POST.getlist("checkedbox")
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))
				todo.status = 1
				todo.save()

		if "taskDelete" in request.POST:
			checkedlist = request.POST.getlist("checkedbox")
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))
				todo.delete()
	context = { "taskEditId":taskEditId,
				"taskEditValue":taskEditValue,
				"categoryEditValue":categoryEditValue,
				"dateEditValue":dateEditValue,
				"todos": todos,
				"categories":categories
			  }
	return render(request, "index.html",context)

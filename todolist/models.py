# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields.related import ForeignKey
from django.utils import timezone


# Create your models here.
class Category(models.Model): # The Category table name that inherits models.Model
	name = models.CharField(max_length=100,default="Low") #Like a varchar

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name #name to be shown when called

class TodoList(models.Model): #Todolist able name that inherits models.Model
	created_by = models.IntegerField(null=False)
	title = models.CharField(max_length=250) # a varchar
	content = models.TextField(blank=True) # a text field
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	category = models.ForeignKey(Category, default="Low",on_delete=models.CASCADE) # a foreignkey
	status = models.IntegerField(max_length=20,default=0)

	class Meta:
		ordering = ["due_date"] #ordering by the created field

	def __str__(self):
		return str(self.created_by) + self.title + str(self.created) + str(self.due_date) + str(self.category) + str(self.status) #name to be shown when called

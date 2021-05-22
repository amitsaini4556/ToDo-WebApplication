from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from validate_email import validate_email

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def isValidEmail(self):
		email = self.cleaned_data.get('email')
		if validate_email(email,verify=True) == True:
			try:
				match = User.objects.get(email = email)
			except User.DoesNotExist:
				return email
			raise forms.ValidationError('This email address is already in use.')
		else:
			raise forms.ValidationError('This email address is Invalid.')

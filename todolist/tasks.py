from . models import *
from django.contrib.auth.models import User
import datetime
from django.core.mail import BadHeaderError, send_mail
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def myTask():
    todolist = TodoList.objects.filter(due_date = datetime.date.today() + datetime.timedelta(days = 1),status = 0)
    for todo in todolist:
        toUserEmail = User.objects.only('email').get(id = int(todo.created_by)).email
        toUserName = User.objects.only('username').get(id = int(todo.created_by)).username

        html_template = 'email.html'
        context = {
                    'user': toUserName,
                    'title': todo.title,
                    'dueDate': todo.due_date,
                    'priority':todo.category
                    }
        html_message = render_to_string(html_template, context)
        subject = 'Due task ' + todo.title
        message = EmailMessage(subject, html_message, 'tododjangowebapp@gmail.com', [toUserEmail])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()

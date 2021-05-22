from . models import *
import datetime
from django.core.mail import BadHeaderError, send_mail

def myTask():
    todolist = str(TodoList.objects.filter(due_date = datetime.date.today() + datetime.timedelta(days = 1)))
    send_mail('Due tasks', todolist, 'amitsaini2701@gmail.com', ['amitsaini2701@gmail.com'])
    print(todolist)

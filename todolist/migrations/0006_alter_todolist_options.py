# Generated by Django 3.2 on 2021-05-07 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20210507_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['due_date', 'status']},
        ),
    ]

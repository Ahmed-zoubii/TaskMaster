# Generated by Django 5.1.4 on 2025-02-28 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_rename_user_todo_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='users',
            new_name='user',
        ),
    ]

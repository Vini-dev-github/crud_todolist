# Generated by Django 5.0.6 on 2024-06-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todos', '0003_alter_todo_deadline_alter_todo_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]

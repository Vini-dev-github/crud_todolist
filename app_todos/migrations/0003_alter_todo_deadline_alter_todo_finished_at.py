# Generated by Django 5.0.6 on 2024-06-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todos', '0002_alter_todo_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateField(null=True),
        ),
    ]

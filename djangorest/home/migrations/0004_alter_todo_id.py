# Generated by Django 5.0.2 on 2024-02-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_todo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-20 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='percentage',
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0002_remove_student_percentage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]
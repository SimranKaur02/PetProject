# Generated by Django 3.2.11 on 2022-12-29 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0002_alter_department_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dept',
            new_name='student_dept',
        ),
    ]

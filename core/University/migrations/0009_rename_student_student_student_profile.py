# Generated by Django 3.2.11 on 2022-12-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0008_auto_20221229_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='student_profile',
        ),
    ]

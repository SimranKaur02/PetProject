# Generated by Django 3.2.11 on 2022-12-29 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0009_rename_student_student_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='University.department'),
        ),
    ]
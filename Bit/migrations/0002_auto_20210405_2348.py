# Generated by Django 3.1.7 on 2021-04-05 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='course_code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_structure',
            new_name='course_name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='credit_distribution',
        ),
    ]

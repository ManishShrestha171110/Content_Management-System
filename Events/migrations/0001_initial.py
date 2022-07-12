# Generated by Django 3.1.7 on 2021-05-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_and_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'newevents',
                'verbose_name_plural': 'newevents',
            },
        ),
    ]

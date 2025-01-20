# Generated by Django 5.0.4 on 2024-05-11 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0001_initial'),
        ('employee', '0010_rename_submission_datetime_submission_saved_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeeinfo')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

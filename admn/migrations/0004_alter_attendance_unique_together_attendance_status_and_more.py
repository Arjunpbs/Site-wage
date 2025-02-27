# Generated by Django 5.0.4 on 2024-05-28 14:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0003_attendance'),
        ('employee', '0012_alter_logotsave_saved_datetime_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employee', 'date')},
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('P', 'Present'), ('A', 'Absent')], default='A', max_length=1),
        ),
        migrations.CreateModel(
            name='Attendanceregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_present', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeeinfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='is_present',
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_addattendance_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addattendance',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

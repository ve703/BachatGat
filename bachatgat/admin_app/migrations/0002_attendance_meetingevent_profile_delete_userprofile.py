# Generated by Django 4.1.10 on 2023-08-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_present', models.BooleanField(default=False)),
            ],
        )
       
        
        
    ]

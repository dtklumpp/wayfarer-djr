# Generated by Django 3.1.2 on 2020-10-13 19:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('posted_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
    ]

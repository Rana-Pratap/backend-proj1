# Generated by Django 4.0.4 on 2022-06-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('uname', models.CharField(max_length=35)),
                ('addRe', models.TextField()),
                ('cityn', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('pinco', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Info',
            },
        ),
    ]

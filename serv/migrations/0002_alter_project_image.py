# Generated by Django 4.1.4 on 2022-12-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

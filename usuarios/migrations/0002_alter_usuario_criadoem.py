# Generated by Django 3.2.8 on 2021-10-09 17:45
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='criadoem',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

# Generated by Django 3.0.6 on 2020-08-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_db',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 5.1 on 2024-09-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

# Generated by Django 2.2.10 on 2020-05-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200521_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notepad',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

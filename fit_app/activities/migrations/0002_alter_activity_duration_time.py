# Generated by Django 4.0.3 on 2022-03-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration_time',
            field=models.IntegerField(),
        ),
    ]

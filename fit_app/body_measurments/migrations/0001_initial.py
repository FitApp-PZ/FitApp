# Generated by Django 4.0.3 on 2022-03-29 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_goal', models.FloatField()),
                ('created_at_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'goals',
            },
        ),
        migrations.CreateModel(
            name='BodyMeasurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('date', models.DateField()),
                ('created_at_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_measurements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'body measurements',
            },
        ),
        migrations.CreateModel(
            name='BodyCircuits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neck', models.FloatField()),
                ('hips', models.FloatField()),
                ('chest', models.FloatField()),
                ('biceps', models.FloatField()),
                ('thigh', models.FloatField()),
                ('waist', models.FloatField()),
                ('calf', models.FloatField()),
                ('belly', models.FloatField()),
                ('date', models.DateField()),
                ('created_at_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_circuits', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'body circuits',
            },
        ),
    ]

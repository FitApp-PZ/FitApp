# Generated by Django 4.0.3 on 2022-03-22 13:16

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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Bieganie'), (2, 'Jazda na rowerze'), (3, 'Trening siłowy'), (4, 'Piłka nożna'), (5, 'Koszykówka'), (6, 'Badminton'), (7, 'Skakanka'), (8, 'Joga'), (9, 'Tenis'), (10, 'Boks')], default=3)),
                ('duration_time', models.TimeField()),
                ('date', models.DateField()),
                ('created_at_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
    ]

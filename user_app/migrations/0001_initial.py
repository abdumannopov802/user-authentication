# Generated by Django 5.0.4 on 2024-04-04 13:15

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('interests', models.CharField(blank=True, choices=[('sports', 'Sports'), ('music', 'Music'), ('books', 'Books'), ('movies', 'Movies'), ('travel', 'Travel'), ('food', 'Food')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_category', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('children', 'Children')], max_length=10)),
                ('product_category', models.CharField(choices=[('sports', 'Sports'), ('music', 'Music'), ('books', 'Books'), ('movies', 'Movies'), ('travel', 'Travel'), ('food', 'Food')], max_length=10)),
                ('from_age', models.DateField()),
                ('under_age', models.DateField()),
            ],
        ),
    ]

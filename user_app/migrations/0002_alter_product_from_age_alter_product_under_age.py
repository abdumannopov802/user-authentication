# Generated by Django 5.0.4 on 2024-04-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='from_age',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='under_age',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_skintheme'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='skins',
            field=models.ManyToManyField(to='main_app.skintheme'),
        ),
    ]

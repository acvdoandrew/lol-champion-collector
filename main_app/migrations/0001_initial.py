# Generated by Django 4.1.2 on 2022-10-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('epithet', models.TextField(max_length=100)),
                ('hours', models.IntegerField()),
            ],
        ),
    ]

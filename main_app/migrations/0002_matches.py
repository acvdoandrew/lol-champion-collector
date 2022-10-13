# Generated by Django 4.1.2 on 2022-10-13 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='match date')),
                ('match', models.CharField(choices=[('V', 'VICTORY'), ('D', 'DEFEAT')], default='V', max_length=1)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.champion')),
            ],
        ),
    ]

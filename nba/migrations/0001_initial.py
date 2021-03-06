# Generated by Django 2.2.6 on 2019-10-27 23:33

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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=30)),
                ('away_team', models.CharField(max_length=30)),
                ('home_spread', models.FloatField(null=True)),
                ('away_spread', models.FloatField(null=True)),
                ('date_time', models.DateTimeField()),
                ('neutral', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(max_length=40)),
                ('outcome', models.CharField(choices=[('win', 'win'), ('loss', 'loss'), ('push', 'push')], max_length=5, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
